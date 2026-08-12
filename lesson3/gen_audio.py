import asyncio, edge_tts, os

OUT = r"D:\EHS英语资料\_deploy\lesson3\audio3"
VOICE = "en-US-AriaNeural"
os.makedirs(OUT, exist_ok=True)

tasks = []
collocs = {
    "basic": ["housekeeping restoration","temporary facilities","site walkthrough","potential hazards","lock out tag out","flammable materials","designated storage","site handover"],
    "prequal": ["work permits","corrective actions","full-cycle records","OSHA compliance","training records","safety meeting minutes","joint acceptance","vehicle departure"],
    "prejob": ["performance evaluation","leading indicators","lagging indicators","near-miss reporting","corrective action closure rate","training completion rate","QBR score","qualified contractor list"]
}
for lvl, phrases in collocs.items():
    for i, p in enumerate(phrases):
        tasks.append((f"colloc_{lvl}_{i}.mp3", p))

dialogues = {
    "basic": [
        "The project is almost finished. What full-site safety close-out work should we arrange first?",
        "The contractor leads a full-site self-inspection. They need to restore housekeeping and dismantle all temporary safety facilities.",
        "I will verify all LOTO energy isolation points are formally removed.",
        "We will walk through the site to check for potential hazards like leftover flammable materials and sharp objects.",
        "All construction waste must be cleared and disposed of per regulatory requirements before site handover."
    ],
    "prequal": [
        "After site cleanup, do they need to keep documents on file for mandatory requirements?",
        "All high-risk work permits must be fully closed out. All identified hazards and corrective actions must be 100 percent signed off.",
        "We archive full-cycle EHS records for OSHA review, including training records and safety meeting minutes.",
        "Can we move equipment off-site once paperwork is done?",
        "EHS, PM and facility do a three-party joint safety acceptance. Only after passing can you start vehicle departure procedures."
    ],
    "prejob": [
        "After project handover, how do we assess this contractor safety performance?",
        "We use a performance evaluation form covering housekeeping, PPE, fall protection, chemical management and work permit execution.",
        "Is safety included in their quarterly business review?",
        "EHS accounts for 20 percent of the total QBR score. Top-rated contractors get bid priority; poor performers face restriction or removal from the qualified contractor list.",
        "What indicators make up the 20 percent EHS weighting?",
        "We prioritize leading indicators like inspection rates, training completion rate and proactive near-miss reporting, not just lagging indicators like injury rates."
    ]
}
for lvl, lines in dialogues.items():
    for i, line in enumerate(lines):
        tasks.append((f"dialog_{lvl}_{i}.mp3", line))

async def gen_one(fname, text):
    path = os.path.join(OUT, fname)
    if os.path.exists(path):
        print(f"  SKIP {fname}")
        return
    comm = edge_tts.Communicate(text, VOICE)
    await comm.save(path)
    print(f"  OK   {fname}")

async def main():
    print(f"Generating {len(tasks)} audio files...")
    for i in range(0, len(tasks), 4):
        await asyncio.gather(*[gen_one(f, t) for f, t in tasks[i:i+4]])
    print(f"Done! {len(tasks)} files in {OUT}")

asyncio.run(main())
