from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Msg(BaseModel):
    msg: str

i
@app.get("/anthracnose")
async def root():
    return {"DESCRIPTION": "Antracnose is a fungal disease that affects a wide range of plants, including mango trees. It is caused by several species of fungi in the Colletotrichum genus, which can infect the leaves, stems, flowers, and fruit of the tree. Symptoms of antracnose on mango trees include small, dark-colored spots on the leaves, stems, and fruit.", "LETHALITY": "Not lethal, moderate", "HUMIDITY": "Warm and moist weather"}


@app.get("/sootymold")
async def root():
    return {"DESCRIPTION": "Dark Brown, Black mostly seen in Warm and Dry period and  grows on honeydew excreted by piercing sucking insects.", "LETHALITY": "Not lethal, Mild, Moderate", "HUMIDITY": "Warm or Dry Weather."}


@app.get("/redrust")
async def root():
    return {"DESCRIPTION": "Red rust is a fungal disease that damages mango plants. Puccinia mangiferae affects the tree's leaves. Reddish-brown or orange pustules on the leaves may cause distortion and premature leaf drop. This reduces tree growth and fruit yield.", "LETHALITY": "Not lethal, Mild, Moderate", "HUMIDITY": "Wet and warm weather"}



@app.get("/path")
async def demo_get():
    return {"message": "This is /path endpoint, use a post request to transform the text to uppercase"}


@app.post("/path")
async def demo_post(inp: Msg):
    return {"message": inp.msg.upper()}


@app.get("/path/{path_id}")
async def demo_get_path_id(path_id: int):
    return {"message": f"This is /path/{path_id} endpoint, use post request to retrieve result"}