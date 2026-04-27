#!/usr/bin/env python3
"""Generate Weston Creek suburb pages for EcoMow Canberra."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from generate_belconnen import TEMPLATE, REVIEWS

SUBURBS = [
    {
        "name": "Chapman",
        "slug": "chapman",
        "postcode": "2611",
        "region": "Weston Creek",
        "hero_lead": "Chapman sits up against the Molonglo River corridor and the Cooleman Ridge nature reserve — it's one of those suburbs where backyards merge into bushland and kangaroos regularly graze on the front verge. Larger blocks, mature natives mixed with established garden plantings, and the kind of terrain that needs someone who understands slope and aspect.",
        "why_paragraph": "Chapman properties often back onto reserve land or have steep sections that change how the grass grows. We adjust mowing heights for slope, manage the native-garden interface carefully, and know how to deal with the kangaroo damage that Chapman lawns cop regularly — compacted soil, grazing patches, and roo paths worn into the turf.",
        "job_title": "Chapman bushland-edge garden tidy",
        "job_description": "Large rear garden backing onto Cooleman Ridge — mowed the accessible lawn areas, cleared kangaroo-damaged patches with a light rake and overseed, edged the boundary where grass meets native ground cover, and trimmed overhanging branches from the back fence. Blower finish on the patio and paths.",
        "nearby": ["rivett", "fisher", "duffy", "stirling"],
        "scheduling": "Usually within the week for Chapman",
    },
    {
        "name": "Duffy",
        "slug": "duffy",
        "postcode": "2611",
        "region": "Weston Creek",
        "hero_lead": "Duffy is the westernmost suburb in Weston Creek — right up against the Molonglo River and Stromlo Forest Park. A lot of properties here have expansive views, larger blocks, and gardens that range from fully established 1970s plantings to bush-adjacent native landscapes. Good community feel with the Duffy shops and primary school anchoring the suburb.",
        "why_paragraph": "Duffy's position near Stromlo means fire-season preparation is on a lot of homeowners' minds. We help keep the property tidy and defensible — clearing leaf litter from gutters and fence lines, maintaining clearance around structures, and keeping lawns short heading into summer. Practical stuff that matters out here.",
        "job_title": "Duffy pre-summer fire prep tidy",
        "job_description": "Full property preparation before fire season — gutters cleared, all leaf litter raked from fence lines and around the house perimeter, lawn mowed short, overhanging branches trimmed back from the roof line, and two trailer loads of accumulated green waste removed. Peace of mind before the hot months.",
        "nearby": ["holder", "rivett", "chapman", "weston"],
        "scheduling": "Usually within the week for Duffy",
    },
    {
        "name": "Fisher",
        "slug": "fisher",
        "postcode": "2611",
        "region": "Weston Creek",
        "hero_lead": "Fisher is a small, quiet suburb in the heart of Weston Creek — mostly family homes built in the late 1970s on good-sized blocks with established gardens. It sits between Waramanga and Chapman with easy access to Cooleman Court shops. The kind of suburb where a tidy front garden genuinely lifts the whole street.",
        "why_paragraph": "Fisher's compact layout means we're often doing multiple jobs on the same street or neighbouring blocks in a single visit. That efficiency gets passed on — no travel premium, quick scheduling, and we're already in the area most weeks servicing regular customers.",
        "job_title": "Fisher street cluster — three properties in one visit",
        "job_description": "Three neighbouring Fisher properties serviced in a single morning — full mow and edge on all three, one hedge trim along a shared boundary, and nature strips done to a consistent height across all frontages. Neighbours coordinating their bookings makes everyone's price better.",
        "nearby": ["waramanga", "chapman", "rivett"],
        "scheduling": "Usually within the week for Fisher",
    },
    {
        "name": "Holder",
        "slug": "holder",
        "postcode": "2611",
        "region": "Weston Creek",
        "hero_lead": "Holder wraps around the western side of Cooleman Court — Weston Creek's main shops precinct. It's a mix of original 1970s family homes, some townhouse developments, and a few larger blocks that back onto the Molonglo River corridor. Close to everything in Weston Creek while still feeling residential and quiet.",
        "why_paragraph": "Holder has a good mix of property types — from compact townhouse courtyards near the shops to bigger standalone blocks on the western edge. We price each job on what's actually there, not a one-size-fits-all rate. A small courtyard mow costs what it should, and a large block gets the time it needs.",
        "job_title": "Holder townhouse courtyard maintenance",
        "job_description": "Compact courtyard garden at a Holder townhouse — mowed the small lawn area, edged the patio border, weeded the front garden bed, trimmed the low hedge along the front path, and blew down all hard surfaces. Took under an hour, priced accordingly. Monthly visits set up.",
        "nearby": ["duffy", "weston", "rivett", "stirling"],
        "scheduling": "Usually within the week for Holder",
    },
    {
        "name": "Rivett",
        "slug": "rivett",
        "postcode": "2611",
        "region": "Weston Creek",
        "hero_lead": "Rivett is central Weston Creek — established family homes on decent blocks, well-maintained streets, and a suburban character that's settled and comfortable. The Rivett shops give it a local centre, and most homes have had forty-plus years for their gardens to mature. Hedges are big, trees are tall, and lawns are well-established.",
        "why_paragraph": "Rivett's mature gardens mean serious hedge work — forty-year-old photinias, viburnum screens, and boundary hedges that need proper shaping rather than a quick hack. We bring the right battery hedge trimmers for the job and leave clean, straight lines with all clippings removed.",
        "job_title": "Rivett boundary hedge reshape",
        "job_description": "Long rear boundary hedge — old-growth viburnum that had grown up and out over several seasons. Reshaped all accessible faces to a clean line, reduced the height by about 300mm, collected and removed all clippings. The neighbour asked for our number before we'd finished.",
        "nearby": ["fisher", "holder", "chapman", "stirling"],
        "scheduling": "Usually within the week for Rivett",
    },
    {
        "name": "Stirling",
        "slug": "stirling",
        "postcode": "2611",
        "region": "Weston Creek",
        "hero_lead": "Stirling is on the eastern edge of Weston Creek, bordering Curtin and the Woden Valley. The suburb feels a bit different from the rest of Weston Creek — slightly more elevated, with some properties offering views across to the Brindabellas. Good-sized blocks with a mix of original gardens and some that have been completely redesigned over the years.",
        "why_paragraph": "Stirling's elevated position means more exposure to wind and sun than the lower Weston Creek suburbs. Lawns dry out faster on the north-facing slopes, and hedges on the ridgeline cop more weather. We factor that in — adjusted mowing heights on exposed sections, and timing visits to avoid the worst of the afternoon westerly that makes blowing pointless.",
        "job_title": "Stirling exposed front yard recovery",
        "job_description": "North-facing front lawn that had dried out and thinned over summer — aerated the compacted areas, top-dressed with a compost and sand mix, overseeded with a drought-tolerant couch blend, and set up a fortnightly mowing schedule at a higher cut to help recovery through autumn.",
        "nearby": ["holder", "rivett", "curtin", "weston"],
        "scheduling": "Usually within the week for Stirling",
    },
    {
        "name": "Waramanga",
        "slug": "waramanga",
        "postcode": "2611",
        "region": "Weston Creek",
        "hero_lead": "Waramanga is the northern gateway to Weston Creek — sitting right between the Weston Creek area and Belconnen's southern suburbs. It's a quiet, well-treed suburb with established 1970s homes, generous nature strips, and the kind of neighbourhood where people walk their dogs and wave at the mower guy. We're in Waramanga regularly.",
        "why_paragraph": "Waramanga's wide nature strips and generous frontages mean the verge is a real part of how the property looks from the street. We include verge mowing and edging as standard when we do the front — no point leaving a tidy lawn next to a shaggy nature strip. The whole frontage gets done properly.",
        "job_title": "Waramanga full frontage — lawn, verge and hedge",
        "job_description": "Complete front-of-house service — mowed the front lawn and both nature strips, edged along the footpath and kerb, trimmed the front hedge to a clean line, weeded the garden bed under the front window, and blew down the driveway and path. Street presence transformed.",
        "nearby": ["fisher", "stirling", "holder"],
        "scheduling": "Usually within the week for Waramanga",
    },
    {
        "name": "Weston",
        "slug": "weston",
        "postcode": "2611",
        "region": "Weston Creek",
        "hero_lead": "Weston is one of the oldest suburbs in the Weston Creek area — some of the most established gardens in the district are right here. The blocks are generous, the trees are massive, and the gardens reflect decades of care. With Cooleman Court nearby and the creek corridor running through, it's a suburb with real character and proper green infrastructure.",
        "why_paragraph": "Weston's mature tree canopy creates heavy shade in a lot of backyards, which changes everything about how the lawn grows. We adjust mowing heights for shaded areas, recommend shade-tolerant grass varieties when reseeding, and manage the leaf drop that comes with those big established trees — especially the deciduous ones that dump everything in April.",
        "job_title": "Weston autumn leaf and lawn service",
        "job_description": "Massive deciduous tree dumping leaves across the entire backyard and into the gutters. Full leaf clearing with battery blower, gutters cleaned, lawn mowed underneath once cleared, and all leaves bagged and removed. Four green bins worth. Booked in for a repeat visit in three weeks when the next wave hits.",
        "nearby": ["holder", "duffy", "stirling"],
        "scheduling": "Usually within the week for Weston",
    },
]

def generate():
    base = os.path.dirname(os.path.abspath(__file__))
    suburbs_dir = os.path.join(base, "suburbs")
    for i, suburb in enumerate(SUBURBS):
        review = REVIEWS[i % len(REVIEWS)]
        nearby_links = []
        for ns in suburb["nearby"]:
            # Simple display name lookup
            name_map = {"rivett":"Rivett","fisher":"Fisher","duffy":"Duffy","chapman":"Chapman",
                        "holder":"Holder","stirling":"Stirling","waramanga":"Waramanga","weston":"Weston",
                        "curtin":"Curtin"}
            display = name_map.get(ns, ns.replace("-"," ").title())
            nearby_links.append(f'      <a href="/suburbs/{ns}/">{display}</a>')
        html = TEMPLATE.format(
            name=suburb["name"], slug=suburb["slug"], postcode=suburb["postcode"],
            region=suburb["region"], hero_lead=suburb["hero_lead"],
            why_paragraph=suburb["why_paragraph"], job_title=suburb["job_title"],
            job_description=suburb["job_description"], scheduling=suburb["scheduling"],
            review_quote=review[0], review_name=review[1], review_suburb=review[2],
            nearby_links="\n".join(nearby_links),
        )
        suburb_dir = os.path.join(suburbs_dir, suburb["slug"])
        os.makedirs(suburb_dir, exist_ok=True)
        with open(os.path.join(suburb_dir, "index.html"), "w") as f:
            f.write(html)
        print(f"  Created: suburbs/{suburb['slug']}/index.html")
    print(f"\nGenerated {len(SUBURBS)} Weston Creek suburb pages.")

if __name__ == "__main__":
    generate()
