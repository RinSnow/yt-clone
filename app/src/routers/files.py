"""This module contains the routes for file uploads."""

from typing import Annotated
from fastapi import APIRouter, File, UploadFile
from fastapi.responses import HTMLResponse


router = APIRouter()


@router.post("/files/")
async def create_files(
    files: Annotated[list[bytes], File(description="Multiple files as bytes")],
):
    """Basic file upload."""
    return {"file_sizes": [len(file) for file in files]}


@router.post("/uploadfile/")
async def create_upload_file(myfile: UploadFile = File(...)):
    """Upload file in chunks."""
    file_size = myfile.spool_max_size
    print(file_size)
    with open(f"../uploads/{myfile.filename}", "wb") as buffer:
        while True:
            chunk = await myfile.read(2024)  # Read in 1KB chunks
            print(len(chunk))
            if not chunk:
                break
            buffer.write(chunk)
    return {"filename": myfile.filename}


@router.get("/")
async def main():
    """Main page for file uploads."""
    content = """
<body>
<form action="/files/" enctype="multipart/form-data" method="post">
<input name="files" type="file" multiple>
<input type="submit">
</form>
<form action="/uploadfile/" enctype="multipart/form-data" method="post">
<input name="myfile" type="file" multiple>
<input type="submit">
</form>
</body>
    """
    return HTMLResponse(content=content)
