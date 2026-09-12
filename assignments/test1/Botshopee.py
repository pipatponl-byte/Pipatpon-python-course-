import os
import sys
import whisper


def process_video_to_text(video_path: str, output_txt_path: str):
    # ตรวจสอบว่ามีไฟล์วิดีโออยู่ในโฟลเดอร์หรือไม่
    if not os.path.exists(video_path):
        print(f"Error: ไม่พบไฟล์ '{video_path}' ในโฟลเดอร์ปัจจุบัน")
        return

    print("กำลังโหลดโมเดล Whisper (Base)...")
    model = whisper.load_model("base")

    print(f"กำลังประมวลผลถอดเสียงจากไฟล์ {video_path} ...")
    # ถอดเสียงโดยระบุภาษาไทย (หากต้องการให้ออโต้ตรวจจับ สามารถลบ language="th" ออกได้)
    result = model.transcribe(video_path, language="th")

    # บันทึกผลลัพธ์ลงไฟล์ .txt
    with open(output_txt_path, "w", encoding="utf-8") as f:
        f.write(result["text"])

    print("\n" + "=" * 40)
    print("ประมวลผลเสร็จสิ้น!")
    print("=" * 40)
    print(f"บันทึกไฟล์ข้อความเรียบร้อยแล้วที่: {output_txt_path}")
    print("\nข้อความที่ถอดได้จากคลิป:")
    print(result["text"])


if __name__ == "__main__":
    # ระบุชื่อไฟล์วิดีโอและไฟล์ข้อความผลลัพธ์
    VIDEO_FILE = "video_1.mp4"
    OUTPUT_FILE = "output.txt"

    process_video_to_text(VIDEO_FILE, OUTPUT_FILE)