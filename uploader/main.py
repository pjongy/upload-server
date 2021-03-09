import os
import random
import time
import string
from typing import List, Optional

from fastapi import FastAPI, File, UploadFile, HTTPException, Header
from aiofile import AIOFile, Writer


upload_directory = os.environ['UPLOAD_PATH']
access_token = os.environ['ACCESS_TOKEN']

try:
    os.mkdir(upload_directory)
    print(os.getcwd())
except Exception as e:
    print(e)


def random_string_with_time(length: int):
    return ''.join(
        random.choices(string.ascii_lowercase + string.digits, k=length)
    ) + '-' + str(int(time.time()))


async def store_file(uploaded_file: UploadFile, destination: string):
    async with AIOFile(os.path.join(upload_directory, destination), 'wb') as f:
        writer = Writer(f)
        while True:
            chunk = await uploaded_file.read(8192)
            if not chunk:
                break
            await writer(chunk)
    return destination


app = FastAPI()


@app.post("/files")
async def upload_files(
    files: List[UploadFile] = File(...),
    authorization: Optional[str] = Header(None),
):
    if authorization != f'Basic {access_token}':
        raise HTTPException(
            status_code=403,
            detail=f'Invalid token in header should Authorization: Basic XX'
        )
    result = []
    for uploaded_file in files:
        filename = uploaded_file.filename
        extension = filename.split('.')[-1]
        stored_filename = random_string_with_time(10) + '.' + extension
        await store_file(uploaded_file, stored_filename)
        result.append({'original': filename, 'stored': stored_filename})
    return {'files': result}
