import webuiapi
from PIL import Image
from config_loader import load_config
from config_loader import change_count

protocol, domain, port, url = load_config()
api = webuiapi.WebUIApi(host=domain, port=port)

def start_generate():
    try:
        result1 = Image.open('../images/me.jpg')

        result2 = api.img2img(
            images=[result1], 
            prompt="human, knife", 
            seed=672055811, 
            steps=20,
            cfg_scale=7, 
            denoising_strength=0.6, 
            sampler_name="Euler a",
        )

        count = change_count()
        print(f"The picture output{count}.png has been successfully generated")
        result2.image.save(f'../images/output/output{count}.png')
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    start_generate()