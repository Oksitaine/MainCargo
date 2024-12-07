import os
import subprocess


PATH_TO_MOUNT = "/workspace"
PATH_TO_COMFY = "/app/src/ComfyUI"

class InstallModel:
    def __init__(self, namemodel, models, huggingface_token = ""):
        self.models = models
        self.namemode = namemodel
        self.huggingface_token = huggingface_token
        if huggingface_token == "":
            raise ValueError("Please provide a valid huggingface token")
    
        self.install_model()

    def install_model(self):
        print(f"Installing and config {self.namemode} models...")

        if not os.path.exists(PATH_TO_MOUNT):
            raise ValueError(f"Path {PATH_TO_MOUNT} does not exist, create a mount folder")
        
        for model in self.models:
            if not os.path.exists(model["path_comfy"]):
                print(f"---------- Installing {model["name"]} ----------")
                if not os.path.exists(model["path_mount"]):
                    print("Downloading model...")
                    subprocess.run([
                        "wget",
                        "--header",
                        f"Authorization: Bearer {self.huggingface_token}",
                        model["URL"],
                        "-O",
                        model["name"]
                    ], cwd=PATH_TO_MOUNT)
                
                print("copy file...")
                subprocess.run([
                    "cp",
                    "-v",
                    model["path_mount"],
                    model["path_comfy"]
                ])


if __name__ == "__main__":    
    # ------------------------ Description -------------------------
    #
    # Install and Config Flux 1 DEV models ( DoubleCLIP + VAE + DIFFUSERS MODEL )
    #
    # ------------------------ Description -------------------------
    FLUX_1_DEV = [
        {
            "name": "flux1-dev.safetensors",
            "path_mount": f"{PATH_TO_MOUNT}/flux1-dev.safetensors",
            "path_comfy": f"{PATH_TO_COMFY}/models/unet/flux1-dev.safetensors",
            "URL": "https://huggingface.co/black-forest-labs/FLUX.1-dev/resolve/main/flux1-dev.safetensors"
        },
        {
            "name": "ae.safetensors",
            "path_mount": f"{PATH_TO_MOUNT}/ae.safetensors",
            "path_comfy": f"{PATH_TO_COMFY}/models/vae/ae.safetensors",
            "URL": "https://huggingface.co/black-forest-labs/FLUX.1-dev/resolve/main/ae.safetensors"
        },
        {
            "name": "clip_l.safetensors",
            "path_mount": f"{PATH_TO_MOUNT}/clip_l.safetensors",
            "path_comfy": f"{PATH_TO_COMFY}/models/clip/clip_l.safetensors",
            "URL": "https://huggingface.co/comfyanonymous/flux_text_encoders/resolve/main/clip_l.safetensors"
        },
        {
            "name": "t5xxl_fp8_e4m3fn.safetensors",
            "path_mount": f"{PATH_TO_MOUNT}/t5xxl_fp8_e4m3fn.safetensors",
            "path_comfy": f"{PATH_TO_COMFY}/models/clip/t5xxl_fp8_e4m3fn.safetensors",
            "URL": "https://huggingface.co/comfyanonymous/flux_text_encoders/resolve/main/t5xxl_fp8_e4m3fn.safetensors"         
        },
        {
            "name": "t5xxl_fp16.safetensors",
            "path_mount": f"{PATH_TO_MOUNT}/t5xxl_fp16.safetensors",
            "path_comfy": f"{PATH_TO_COMFY}/models/clip/t5xxl_fp16.safetensors",
            "URL": "https://huggingface.co/comfyanonymous/flux_text_encoders/resolve/main/t5xxl_fp16.safetensors"
        }
    ]

    InstallModel("FLUX_1_DEV", FLUX_1_DEV, "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")