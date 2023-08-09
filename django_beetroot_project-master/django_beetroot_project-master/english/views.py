from django.http import HttpResponse
from django.shortcuts import render
from time import sleep, perf_counter
import httpx
import asyncio
from asgiref.sync import async_to_sync, sync_to_async
async def index(request):
    return HttpResponse("Hello, world! I love async :)")

def http_call_sync():
    start = perf_counter()
    for i in range(1,10):
        sleep(1)
        print(i)

    result = httpx.get("https://rickandmortyapi.com/api/location")
    end = perf_counter()
    print("SYNC func took: ", end - start, " sec")


async def http_call_async():
    start = perf_counter()
    for i in range(1, 10):
        await asyncio.sleep(1)
        print(i)
    async with httpx.AsyncClient() as client:
        result = await client.get("https://rickandmortyapi.com/api/location")
    end = perf_counter()
    print("ASYNC func took: ", end - start, " sec")

def sync_view(request):
    http_call_sync()
    return HttpResponse("Blocking request")

async def async_view(request):
    loop = asyncio.get_event_loop()
    loop.create_task(http_call_async())
    return HttpResponse("Non-blocking request")

async def sync_to_async_view(request):
    loop = asyncio.get_event_loop()
    async_http = sync_to_async(sync_view, thread_sensitive=False)
    loop.create_task(async_http())
    return HttpResponse("Non-blocking request with sync function")

def async_to_sync_view(request):
    http_sync = async_to_sync(http_call_async)
    http_sync()
    return HttpResponse("Blocking request with async function")

def s_jobs(request):
    context = {"name": "Python"}
    return render(request, 'search jobs.html', context)

def services(request):
    return render(request, "services.html")