import pytest

from langchain import llms

EXPECTED_DEPRECATED_IMPORTS = [
    "AI21",
    "AlephAlpha",
    "AmazonAPIGateway",
    "Anthropic",
    "Anyscale",
    "Arcee",
    "Aviary",
    "AzureMLOnlineEndpoint",
    "AzureOpenAI",
    "Banana",
    "Baseten",
    "Beam",
    "Bedrock",
    "CTransformers",
    "CTranslate2",
    "CerebriumAI",
    "ChatGLM",
    "Clarifai",
    "Cohere",
    "Databricks",
    "DeepInfra",
    "DeepSparse",
    "EdenAI",
    "FakeListLLM",
    "Fireworks",
    "ForefrontAI",
    "GigaChat",
    "GPT4All",
    "GooglePalm",
    "GooseAI",
    "GradientLLM",
    "HuggingFaceEndpoint",
    "HuggingFaceHub",
    "HuggingFacePipeline",
    "HuggingFaceTextGenInference",
    "HumanInputLLM",
    "KoboldApiLLM",
    "LlamaCpp",
    "TextGen",
    "ManifestWrapper",
    "Minimax",
    "MlflowAIGateway",
    "Modal",
    "MosaicML",
    "Nebula",
    "NIBittensorLLM",
    "NLPCloud",
    "Ollama",
    "OpenAI",
    "OpenAIChat",
    "OpenLLM",
    "OpenLM",
    "PaiEasEndpoint",
    "Petals",
    "PipelineAI",
    "Predibase",
    "PredictionGuard",
    "PromptLayerOpenAI",
    "PromptLayerOpenAIChat",
    "OpaquePrompts",
    "RWKV",
    "Replicate",
    "SagemakerEndpoint",
    "SelfHostedHuggingFaceLLM",
    "SelfHostedPipeline",
    "StochasticAI",
    "TitanTakeoff",
    "TitanTakeoffPro",
    "Tongyi",
    "VertexAI",
    "VertexAIModelGarden",
    "VLLM",
    "VLLMOpenAI",
    "Writer",
    "OctoAIEndpoint",
    "Xinference",
    "JavelinAIGateway",
    "QianfanLLMEndpoint",
    "YandexGPT",
    "VolcEngineMaasLLM",
    "WatsonxLLM",
]


def test_deprecated_imports() -> None:
    for import_ in EXPECTED_DEPRECATED_IMPORTS:
        with pytest.raises(ImportError) as e:
            getattr(llms, import_)
            assert "langchain_community" in e
    with pytest.raises(AttributeError):
        getattr(llms, "foo")
