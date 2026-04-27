#!/usr/bin/env python3
"""Generate Molonglo Valley suburb pages for EcoMow Canberra."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from generate_belconnen import TEMPLATE, REVIEWS

SUBURBS = [
    {
        "name": "Coombs",
        "slug": "coombs",
        "postcode": "2611",
        "region": "Molonglo Valley",
        "hero_lead": "Coombs was one of the first suburbs in the Molonglo Valley development — Canberra's newest district, built from 2016 onwards along the Molonglo River corridor between Weston Creek and Belconnen. Modern, compact housing with a focus on sustainability and community design. The gardens are young, the streetscapes are still maturing, and the suburb has a fresh, contemporary feel.",
        "why_paragraph": "Coombs' compact blocks and modern design mean tight access between properties, narrow side passages, and small but visible front gardens where every detail counts. Our battery-powered gear is ideal here — quiet enough for the close-proximity housing, light enough for tight access, and precise enough for the detailed work that small gardens demand. No exhaust fumes drifting into the neighbour's open window.",
        "job_title": "Coombs compact courtyard — precision garden care",
        "job_description": "Modern Coombs townhouse — small front garden mowed and edged with precision, narrow side passage line-trimmed, compact rear courtyard lawn done, garden beds weeded, and all hard surfaces blown clean. The whole property takes thirty minutes, but the close-quarters work demands attention to detail. Battery gear makes it possible without disturbing the neighbours.",
        "nearby": ["wright", "denman-prospect"],
        "scheduling": "Usually within the week for Coombs",
    },
    {
        "name": "Denman Prospect",
        "slug": "denman-prospect",
        "postcode": "2611",
        "region": "Molonglo Valley",
        "hero_lead": "Denman Prospect is Molonglo Valley's premium address — elevated, with commanding views across the valley and toward the Brindabellas. The Denman Village shops are the social hub, and the housing ranges from architecturally designed homes to quality townhouses. This is one of the most sought-after new suburbs in Canberra, and the presentation standards reflect that.",
        "why_paragraph": "Denman Prospect homeowners invest in their properties and expect a garden service that matches. We deliver premium results — clean mowing patterns, crisp edges, precise hedge work, and a finish that complements the quality of the homes. The elevated, exposed site also means wind management and soil retention matter on the steeper blocks. We factor all of that into how we work each property.",
        "job_title": "Denman Prospect premium home — presentation-grade service",
        "job_description": "Architecturally designed Denman Prospect home — mowed the front and rear lawns with a striped finish, precision-edged all borders and the designer garden bed outlines, trimmed the feature hedges to exact geometric shapes, cleared wind-deposited debris from the entertaining deck, and blew down the long driveway. Premium property, premium finish.",
        "nearby": ["coombs", "wright", "molonglo"],
        "scheduling": "Usually within the week for Denman Prospect",
    },
    {
        "name": "Molonglo",
        "slug": "molonglo",
        "postcode": "2611",
        "region": "Molonglo Valley",
        "hero_lead": "Molonglo is the broader area encompassing the newer development pockets along the Molonglo River — including areas still being released and built out. Properties here range from brand-new builds with fresh landscaping to slightly more established homes in the earlier release areas. The river corridor provides a green spine through the district, and the natural landscape is a genuine feature.",
        "why_paragraph": "The Molonglo area's ongoing development means we work alongside construction — managing gardens that border active building sites, dealing with dust and debris from neighbouring developments, and helping homeowners establish their outdoor spaces despite the construction activity around them. We're experienced at working in developing suburbs and adapting our approach as the area matures.",
        "job_title": "Molonglo new-estate garden establishment",
        "job_description": "New home in a still-developing Molonglo pocket — cleared construction debris that had blown onto the property, mowed the freshly laid turf at establishment height, edged the new paths, hand-weeded the builder-installed garden beds, and cleaned dust deposits off the hard surfaces. Set up a regular schedule to keep the new garden on track while the surrounding area continues to develop.",
        "nearby": ["denman-prospect", "coombs", "wright"],
        "scheduling": "Usually within the week for Molonglo",
    },
    {
        "name": "Whitlam",
        "slug": "whitlam",
        "postcode": "2611",
        "region": "Molonglo Valley",
        "hero_lead": "Whitlam is one of Molonglo Valley's newer suburbs — modern homes, well-planned streets, and the kind of fresh, contemporary design that characterises the whole Molonglo development. Young families are the dominant demographic, and the gardens are mostly in their early years. Good parks and open spaces, and the suburb is still developing its community identity.",
        "why_paragraph": "Whitlam's young gardens benefit most from consistent, careful maintenance during the establishment period. We see too many new lawns damaged by being cut too short too early, or by irregular mowing that lets the grass get stressed between visits. We set Whitlam properties up on the right schedule with the right mowing heights from the start — it makes a massive difference to how the garden matures.",
        "job_title": "Whitlam young garden — establishment-phase care",
        "job_description": "Whitlam property in its second year — turf now well-rooted but still thickening. Mowed at a slightly elevated height to encourage lateral growth, edged all paths carefully to establish clean border lines, weeded the young garden beds before the weeds could set seed, and applied a light organic fertiliser to the front lawn. Fortnightly visits continuing through the growing season.",
        "nearby": ["coombs", "wright", "denman-prospect"],
        "scheduling": "Usually within the week for Whitlam",
    },
    {
        "name": "Wright",
        "slug": "wright",
        "postcode": "2611",
        "region": "Molonglo Valley",
        "hero_lead": "Wright is one of the more established Molonglo Valley suburbs — among the first in the district to be developed, with properties that now have several years of garden maturation behind them. The suburb sits between Coombs and Denman Prospect, with a mix of housing from apartments to townhouses to standalone homes. The Wright shops provide a local centre, and the community is well-established by Molonglo standards.",
        "why_paragraph": "Wright's relative maturity within Molonglo means the gardens are past the establishment phase and into proper ongoing maintenance. Hedges need their first serious reshaping, lawns are thick enough for standard management, and the garden beds have filled out. We transition Wright gardens from gentle establishment care to full maintenance — the mowing heights come down, the hedge trimming gets more structured, and the service becomes comprehensive.",
        "job_title": "Wright maturing garden — full maintenance transition",
        "job_description": "Wright property entering its fourth year — transitioned from establishment-mode care to full maintenance. Lowered mowing height to standard for the now-established couch lawn, gave the front hedge its first proper structural trim, edged hard against all borders, cleared accumulated mulch spill from the paths, and set up a comprehensive fortnightly maintenance schedule. Garden is ready for the full treatment.",
        "nearby": ["coombs", "denman-prospect", "molonglo"],
        "scheduling": "Usually within the week for Wright",
    },
]

def generate():
    base = os.path.dirname(os.path.abspath(__file__))
    suburbs_dir = os.path.join(base, "suburbs")
    name_map = {s["slug"]: s["name"] for s in SUBURBS}
    for i, suburb in enumerate(SUBURBS):
        review = REVIEWS[i % len(REVIEWS)]
        nearby_links = []
        for ns in suburb["nearby"]:
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
    print(f"\nGenerated {len(SUBURBS)} Molonglo Valley suburb pages.")

if __name__ == "__main__":
    generate()
