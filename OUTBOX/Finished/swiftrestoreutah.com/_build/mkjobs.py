"""mkjobs.py <dl_dir>: write imgjobs.json (hand-picked job photos + one stock/own photo per blog post for the first 70 posts)
and blogimg.json (post key -> image name)."""
import json, os, re, sys
DL = sys.argv[1]
d = json.load(open("src/extract.json", encoding="utf-8"))
PICK = [("swift-logo", "logo-revised-small-3-1920w.png", 300), ("favicon-logo", "logo-revised-small-3-159w.png", 64),
        ("darin-jenks", "Darin_Headshot__282_29-1920w.jpg", 900), ("swift-van", "Swift_Restoration_Truck-1920w.png", 900), ("swift-map", "swift-1920w.png", 1000),
        ("air-mover", "air_mover-1920w.jpg", 820), ("air-scrubbers", "air_movers_and_air_scrubbers_2-1920w.jpg", 820), ("basement-drying", "basement_drying-1920w.jpg", 820),
        ("dehumidifier-air-movers", "air_scrubber_and_air_movers-1920w.jpg", 820), ("containment", "containment_2-d71ca9c5-1920w.jpg", 820), ("containment-bed", "containment_1-555458bb-1920w.jpg", 820),
        ("demo-bathroom", "bathroom_water_damage_restoration__281_29-1920w.png", 1400), ("demo-bathroom-2", "bathroom_water_damage_restoration__283_29-1920w.png", 1400),
        ("demo-open-wall", "damage_restoration_demo_-_open_wall_and_ceiling-1920w.jpg", 1000), ("demo-basement", "basement_flood_mitigation__282_29-1920w.png", 1000),
        ("rebuild-bath", "bathroom_water_damage_-_reconstruction__282_29-1920w.jpg", 768), ("rebuild-bath-2", "bathroom_water_damage_-_reconstruction__281_29-1920w.jpg", 768),
        ("finished-bath", "bathroom_remodeling__281_29-1920w.png", 1100), ("finished-bath-2", "bathroom_remodeling__283_29-1920w.png", 1100), ("finished-bath-3", "bathroom_1-1920w.jpg", 820),
        ("before-remodel", "before_remodel-1920w.jpg", 1192), ("after-remodel", "bedroom_after_remodel__281_29-1920w.jpg", 1400), ("after-remodel-2", "bedroom_after_remodel__282_29-1920w.jpg", 1400),
        ("attic-conversion", "attic_conversion-1920w.jpg", 1600), ("fire-kitchen-rebuilt", "kitchen_reconstruction_after_fire_damage_done_by_Swift_Restoration_and_Remodeling-1920w.jpg", 900),
        ("kitchen-transformation", "a_complete_transformation-1920w.jpg", 900), ("ceiling-leak", "ceiling_2-1920w.jpg", 820), ("living-room-dryout", "Water-Damage-Restoration-2023-10-05-Living_Room-1920w.JPG", 1024),
        ("bedroom-mitigation", "bedroom_water_damage_mitigation-1920w.png", 1400), ("after-restoration", "after_damage_restoration-1920w.jpg", 1100),
        ("case-hyrum", "From_Water_Damage_to_Full_Remodel_A_Kitchen_and_Bathroom_Reconstruction_in_Hyrum-_UT-1920w.jpg", 900), ("case-millcreek", "Full_Sewage_Cleanup_and_Reconstruction_for_a_Millcreek-_Utah_Condo-1920w.jpg", 900),
        ("case-kaysville-flood", "Kaysville_Basement_Flood_Emergency_Storm_Water_Cleanup_and_Mold_Mitigation-1920w.jpg", 900), ("case-kaysville-remodel", "Kaysville_Home_Remodel_New_Kitchen-_Custom_Storage-_and_a_Total_Refresh-1920w.jpg", 900),
        ("case-kaysville-rooms", "Kaysville_Multi-Room_Water_Damage_Restoration-1920w.jpg", 900), ("case-farmington-garage", "New_Roof_and_Garage_Build_for_a_Farmington-_UT_Homeowner-1920w.jpg", 900),
        ("case-layton-basement", "Transforming_a_90s_Basement_Into_a_Modern_Family_Space_in_Layton-_UT__281_29-1920w.jpg", 900), ("case-farmington-basement", "When_Water_Damage_Strikes_A_Complete_Basement_Restoration_in_Farmington-_UT-e048afa3-1920w.jpg", 900)]
SKIP = re.compile(r"625d96296858fd0e77ff6cad|Headshot|logo|iicrc|swift-1920|Truck", re.I)
jobs = [list(x) for x in PICK if os.path.exists(os.path.join(DL, x[1]))]
missing = [x[1] for x in PICK if not os.path.exists(os.path.join(DL, x[1]))]
blog = {}
posts = [k for k in d if k.startswith("restoration_tips_")]
for k in posts[:70]:
    for u in d[k]["imgs"]:
        fn = re.sub(r"[^\w.\-]", "_", re.sub(r"-\d{2,4}x\d{2,4}(?=\.\w+$)", "", u.split("?")[0]).split("/")[-1])[-120:]
        if SKIP.search(fn) or not os.path.exists(os.path.join(DL, fn)): continue
        name = "tip-" + re.sub(r"[^a-z0-9]+", "-", k[18:].lower())[:48].strip("-")
        jobs.append([name, fn, 960]); blog[k] = name; break
json.dump(jobs, open("imgjobs.json", "w"), indent=0)
json.dump(blog, open("blogimg.json", "w"), indent=0)
print(len(jobs), "jobs;", len(blog), "post images; missing:", missing)
