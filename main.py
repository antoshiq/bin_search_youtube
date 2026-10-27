
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from binary_search import get_packed_views, get_packed_comms, get_packed_likes, get_packed_engage

app = FastAPI()

templates = Jinja2Templates("templates")

@app.get("/", response_class=HTMLResponse)
def main(request: Request):

    return templates.TemplateResponse(
        name = "index.html",
        request = request,
        context = {}
    )

@app.get("/results", response_class=HTMLResponse)
def results(views: int = None, likes = None, comms = None, engage = None, request: Request = None):

    if views != None:

        result = get_packed_views(views, 100)

    if likes != None:

        result = get_packed_likes(likes, 100)

    if comms != None:

        result = get_packed_comms(comms, 100)

    if engage != None:

        result = get_packed_engage(engage, 100)


    return templates.TemplateResponse(
        request=request,
        name = "input.html",
        context = {"result": result}
    )

    
    
# "video_id","title","channel_name","channel_id","view_count","like_count","comment_count","published_date","thumbnail"

# sorted_df = df.sort_values(by='published_date', ascending=True)
# print(views_binary_search(100000)[["video_id", "view_count"]].head(10))