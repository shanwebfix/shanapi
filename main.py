from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
# আপনার তৈরি করা স্ক্রিনশট রাউটারটি ইমপোর্ট করা হচ্ছে
from apps.screenshot.router import router as screenshot_router

# এপিআই অ্যাপ সেটআপ
app = FastAPI(
    title="ShanAPI Hub",
    description="ToolxBD এর জন্য তৈরি একটি অল-ইন-ওয়ান এপিআই হাব",
    version="1.0.0"
)

# CORS কনফিগারেশন 
# যাতে আপনার নেক্সট জেএস (Next.js) বা অন্য ফ্রন্টএন্ড থেকে এই এপিআই কল করা যায়
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # প্রোডাকশনে গেলে এখানে আপনার ডোমেইন নাম দেবেন
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# প্রতিটি টুলের রাউটার এখানে রেজিস্টার করতে হবে
# ভবিষ্যতে ২০-৪০টি টুল হলে আপনি এভাবেই নিচে নিচে অ্যাড করবেন
app.include_router(screenshot_router)

# হোম রুট (চেক করার জন্য যে এপিআই লাইভ আছে কি না)
@app.get("/")
def read_root():
    return {
        "status": "Online",
        "project": "ShanAPI",
        "author": "Shan",
        "docs": "/docs" # এখান থেকে আপনি এপিআই টেস্ট করতে পারবেন
    }

# সার্ভার রান করার কনফিগারেশন
if __name__ == "__main__":
    import uvicorn
    # এটি ১২৭.০.০.১:৮০০০ পোর্টে রান হবে
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)