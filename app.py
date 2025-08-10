# app.py
import gradio as gr
import os
import json
from doc_processor import process_file

def handle_upload(files):
    reports = []
    reviewed_paths = []
    for f in files:
        report = process_file(f, out_dir="reviewed_out")
        reports.append(report)
        reviewed_paths.append(report["reviewed_file"])
    combined = {
        "processed_count": len(reports),
        "reports": reports
    }
    os.makedirs("reviewed_out", exist_ok=True)
    json_path = os.path.join("reviewed_out", "combined_report.json")
    with open(json_path, "w", encoding="utf-8") as fh:
        json.dump(combined, fh, indent=2)
    return json.dumps(combined, indent=2), reviewed_paths[0] if reviewed_paths else None

with gr.Blocks() as demo:
    gr.Markdown("## ADGM Corporate Agent — Upload .docx files")
    file_input = gr.File(label="Upload one or more .docx files", file_types=[".docx"], file_count="multiple", type="filepath")
    output_text = gr.Textbox(label="JSON Report", lines=20)
    output_file = gr.File(label="Reviewed .docx (download)", file_types=[".docx"])
    file_input.upload(handle_upload, inputs=[file_input], outputs=[output_text, output_file])

demo.launch()
