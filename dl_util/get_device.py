import torch


def get_device(allow_only_gpu: bool = False) -> str:
    if torch.cuda.is_available():
        return "cuda"
    else:
        if allow_only_gpu:
            message = "GPU is not available"
            raise ValueError(message)
        message = "Warning!: CPU will be used for training."
        print(message, flush=True)
        return "cpu"
