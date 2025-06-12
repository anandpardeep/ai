from typing import Optional, List, Mapping, Any, Dict, Sequence
import requests
import json
from llama_index.core import SimpleDirectoryReader, SummaryIndex
from llama_index.core.callbacks import CallbackManager
from llama_index.core.llms import (
    LLM, CustomLLM, # Use base LLM instead of CustomLLM
    CompletionResponse,
    CompletionResponseGen,
    LLMMetadata,
    ChatMessage,
    ChatResponse,
    ChatResponseGen,
)
from llama_index.core.llms.callbacks import llm_completion_callback, llm_chat_callback
from llama_index.core import Settings
from pydantic import BaseModel
from pydantic import Field
class CompanyLLM(CustomLLM):
    """Custom LLM implementation for company-specific endpoint using base LLM class."""
    api_endpoint: str = Field(default="")
    api_key: str = Field(default="")
    model_name: str = Field(default="company-llm-v1")
    context_window: int = Field(default=4096)
    num_output: int = Field(default=512)
    temperature: float = Field(default=0.7)
    max_tokens: int = Field(default=512)
    timeout: int = Field(default=30)
    
    def __init__(self, **data):
        super().__init__(**data)
    
    @property
    def metadata(self) -> LLMMetadata:
        """Get LLM metadata."""
        return LLMMetadata(
            context_window=self.context_window,
            num_output=self.num_output,
            model_name=self.model_name,
        )

    def _create_payload(self, prompt: str, **kwargs) -> Dict[str, Any]:
        """Create the custom payload for your company's API."""
        # Customize this structure for your API
        payload = {
            "prompt": prompt,
            "model": self.model_name,
            "temperature": kwargs.get("temperature", self.temperature),
            "max_tokens": kwargs.get("max_tokens", self.max_tokens),
            "stop": kwargs.get("stop", []),
        }
        
        # Alternative structures (uncomment and modify as needed):
        
        # Structure 1: Nested parameters
        # payload = {
        #     "input": {
        #         "text": prompt,
        #         "parameters": {
        #             "model": self.model_name,
        #             "temperature": kwargs.get("temperature", self.temperature),
        #             "max_length": kwargs.get("max_tokens", self.max_tokens),
        #         }
        #     }
        # }
        
        # Structure 2: OpenAI-like format
        # payload = {
        #     "messages": [{"role": "user", "content": prompt}],
        #     "model": self.model_name,
        #     "temperature": kwargs.get("temperature", self.temperature),
        #     "max_tokens": kwargs.get("max_tokens", self.max_tokens),
        # }
        
        return payload

    def _create_headers(self) -> Dict[str, str]:
        """Create headers for the API request."""
        return {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.api_key}",
            "User-Agent": "LlamaIndex-CustomLLM/1.0",
            # Add any other headers your API requires:
            # "X-API-Version": "v1",
            # "X-Client-ID": "your-client-id",
        }

    def _extract_response_text(self, response_data: Dict[str, Any]) -> str:
        """Extract the generated text from the API response."""
        # Customize based on your API's response format
        
        # Format 1: Direct text field
        if "text" in response_data:
            return response_data["text"]
        
        # Format 2: Generated text
        if "generated_text" in response_data:
            return response_data["generated_text"]
            
        # Format 3: Content field
        if "content" in response_data:
            return response_data["content"]
        
        # Format 4: OpenAI-style choices
        if "choices" in response_data and len(response_data["choices"]) > 0:
            choice = response_data["choices"][0]
            if "text" in choice:
                return choice["text"]
            if "message" in choice and "content" in choice["message"]:
                return choice["message"]["content"]
        
        # Format 5: Nested output
        if "output" in response_data:
            output = response_data["output"]
            if isinstance(output, str):
                return output
            if isinstance(output, dict) and "text" in output:
                return output["text"]
        
        # Format 6: Response field
        if "response" in response_data:
            response_val = response_data["response"]
            if isinstance(response_val, str):
                return response_val
            if isinstance(response_val, dict) and "text" in response_val:
                return response_val["text"]
        
        # ADD YOUR COMPANY'S SPECIFIC FORMAT HERE:
        # Example:
        # if "your_company_field" in response_data:
        #     return response_data["your_company_field"]["generated_content"]
        
        # Fallback
        print(f"Warning: Unknown response format, keys: {list(response_data.keys())}")
        return str(response_data)

    @llm_completion_callback()
    def complete(
        self, prompt: str, formatted: bool = False, **kwargs: Any
    ) -> CompletionResponse:
        """Generate a completion for the given prompt."""
        try:
            # Create payload and headers
            payload = self._create_payload(prompt, **kwargs)
            headers = self._create_headers()
            
            # Debug output (comment out in production)
            print(f"🔗 API Endpoint: {self.api_endpoint}")
            print(f"📦 Request Payload: {json.dumps(payload, indent=2)}")
            
            # Make the API request
            response = requests.post(
                self.api_endpoint,
                headers=headers,
                json=payload,
                timeout=self.timeout
            )
            
            # Check for HTTP errors
            response.raise_for_status()
            
            # Parse the JSON response
            response_data = response.json()
            
            # Debug output (comment out in production)
            print(f"📨 API Response: {json.dumps(response_data, indent=2)}")
            
            # Extract the generated text
            generated_text = self._extract_response_text(response_data)
            
            if not generated_text or generated_text.strip() == "":
                return CompletionResponse(text="Error: Empty response from API")
            
            return CompletionResponse(text=generated_text)
            
        except requests.exceptions.Timeout:
            error_msg = f"Request timeout after {self.timeout} seconds"
            print(f"❌ Error: {error_msg}")
            return CompletionResponse(text=f"Error: {error_msg}")
            
        except requests.exceptions.HTTPError as e:
            try:
                error_detail = response.json()
                error_msg = f"HTTP {response.status_code}: {error_detail}"
            except:
                error_msg = f"HTTP {response.status_code}: {response.text}"
            print(f"❌ Error: {error_msg}")
            return CompletionResponse(text=f"Error: {error_msg}")
            
        except requests.exceptions.RequestException as e:
            error_msg = f"Request failed: {str(e)}"
            print(f"❌ Error: {error_msg}")
            return CompletionResponse(text=f"Error: {error_msg}")
            
        except json.JSONDecodeError as e:
            error_msg = f"Invalid JSON response: {str(e)}"
            print(f"❌ Error: {error_msg}")
            return CompletionResponse(text=f"Error: {error_msg}")
            
        except Exception as e:
            error_msg = f"Unexpected error: {str(e)}"
            print(f"❌ Error: {error_msg}")
            import traceback
            traceback.print_exc()
            return CompletionResponse(text=f"Error: {error_msg}")

    @llm_completion_callback()
    def stream_complete(
        self, prompt: str, formatted: bool = False, **kwargs: Any
    ) -> CompletionResponseGen:
        """Generate a streaming completion for the given prompt."""
        # Simple implementation - return the complete response
        # You can implement true streaming if your API supports it
        completion_response = self.complete(prompt, formatted=formatted, **kwargs)
        yield completion_response

    @llm_chat_callback()
    def chat(self, messages: Sequence[ChatMessage], **kwargs: Any) -> ChatResponse:
        """Chat interface - converts to completion format."""
        # Convert chat messages to a single prompt
        prompt = self._messages_to_prompt(messages)
        completion_response = self.complete(prompt, **kwargs)
        return ChatResponse(
            message=ChatMessage(role="assistant", content=completion_response.text)
        )

    @llm_chat_callback()
    def stream_chat(
        self, messages: Sequence[ChatMessage], **kwargs: Any
    ) -> ChatResponseGen:
        """Streaming chat interface."""
        prompt = self._messages_to_prompt(messages)
        for completion_response in self.stream_complete(prompt, **kwargs):
            yield ChatResponse(
                message=ChatMessage(role="assistant", content=completion_response.text),
                delta=completion_response.delta,
            )

    def _messages_to_prompt(self, messages: Sequence[ChatMessage]) -> str:
        """Convert chat messages to a single prompt string."""
        prompt_parts = []
        for message in messages:
            role = message.role
            content = message.content
            if role == "system":
                prompt_parts.append(f"System: {content}")
            elif role == "user":
                prompt_parts.append(f"User: {content}")
            elif role == "assistant":
                prompt_parts.append(f"Assistant: {content}")
            else:
                prompt_parts.append(f"{role}: {content}")
        
        return "\n".join(prompt_parts) + "\nAssistant:"


# Factory function
def create_company_llm(
    api_endpoint: str,
    api_key: str,
    model_name: str = "company-model",
    **kwargs
) -> CompanyLLM:
    """Create a CompanyLLM instance."""
    return CompanyLLM(
        api_endpoint=api_endpoint,
        api_key=api_key,
        model_name=model_name,
        **kwargs
    )


# Testing functions
def test_llm_basic():
    """Test basic LLM functionality."""
    print("🧪 Testing Basic LLM Functionality")
    print("-" * 40)
    
    # Replace with your actual endpoint and key
    API_ENDPOINT = "https://your-company-api.com/v1/generate"
    API_KEY = "your-api-key-here"
    
    try:
        # Create LLM
        llm = create_company_llm(
            api_endpoint=API_ENDPOINT,
            api_key=API_KEY,
            model_name="your-model",
            temperature=0.7,
            max_tokens=100
        )
        
        print("✅ LLM instance created successfully!")
        print(f"📋 Model: {llm.model_name}")
        print(f"🌡️  Temperature: {llm.temperature}")
        print(f"🔢 Max tokens: {llm.max_tokens}")
        
        # Test completion
        print("\n🔄 Testing completion...")
        test_prompt = "Hello! Please introduce yourself."
        response = llm.complete(test_prompt)
        print(f"✅ Completion successful!")
        print(f"📝 Response: {response.text[:200]}...")
        
        return llm
        
    except Exception as e:
        print(f"❌ Test failed: {str(e)}")
        import traceback
        traceback.print_exc()
        return None


def test_with_llamaindex(llm):
    """Test LLM with LlamaIndex."""
    print("\n🦙 Testing with LlamaIndex")
    print("-" * 40)
    
    try:
        # Set as global LLM
        Settings.llm = llm
        print("✅ Set as global LLM")
        
        # Create sample document
        from llama_index.core import Document
        
        sample_text = """
        Machine Learning (ML) is a subset of artificial intelligence that focuses on 
        algorithms that can learn from and make predictions or decisions based on data. 
        Popular ML techniques include supervised learning, unsupervised learning, and 
        reinforcement learning. Applications include image recognition, natural language 
        processing, and recommendation systems.
        """
        
        documents = [Document(text=sample_text)]
        
        # Create index
        index = SummaryIndex.from_documents(documents)
        print("✅ Created document index")
        
        # Create query engine
        query_engine = index.as_query_engine()
        print("✅ Created query engine")
        
        # Test query
        query = "What are some applications of machine learning mentioned?"
        response = query_engine.query(query)
        print(f"✅ Query successful!")
        print(f"❓ Query: {query}")
        print(f"📝 Response: {response}")
        
        return True
        
    except Exception as e:
        print(f"❌ LlamaIndex test failed: {str(e)}")
        import traceback
        traceback.print_exc()
        return False


if __name__ == "__main__":
    print("🚀 Custom Company LLM Test Suite")
    print("=" * 50)
    
    # Test basic functionality
    llm = test_llm_basic()
    
    if llm:
        # Test with LlamaIndex
        success = test_with_llamaindex(llm)
        
        if success:
            print("\n🎉 All tests passed!")
        else:
            print("\n⚠️  Basic LLM works, but LlamaIndex integration failed")
    else:
        print("\n❌ Basic LLM test failed")
    
    print("\n" + "=" * 50)
    print("✅ Test suite complete!")