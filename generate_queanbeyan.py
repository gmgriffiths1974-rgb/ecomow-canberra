#!/usr/bin/env python3
"""Generate Queanbeyan suburb pages for EcoMow Canberra."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from generate_belconnen import TEMPLATE, REVIEWS

SUBURBS = [
    {
        "name": "Queanbeyan",
        "slug": "queanbeyan",
        "postcode": "2620",
        "region": "Queanbeyan",
        "hero_lead": "Queanbeyan is Canberra's closest neighbour — right across the border in NSW but functionally part of the Canberra region. The older parts of Queanbeyan have big established blocks, mature gardens, and a township character that predates Canberra itself. A lot of people who work in Canberra live in Queanbeyan, and the demand for reliable garden care is just as strong here.",
        "why_paragraph": "Queanbeyan's older residential areas have some of the largest blocks in the region — heritage-sized lots with gardens that have been growing for generations. We bring the full range of services across the border: regular mowing, hedge trimming, garden cleanups, gutter clearing, and everything else. Same quality, same reliability, same pricing — just a different postcode.",
        "job_title": "Queanbeyan heritage block — large garden service",
        "job_description": "Large heritage-sized block in central Queanbeyan — expansive front lawn, deep backyard, two side passages, and a detached rear garage surrounded by overgrown garden beds. Full mow and edge, three garden beds weeded, overgrown rose bushes pruned back, rear hedge trimmed, and all green waste collected and removed. Two-hour job for a property with real character.",
        "nearby": ["queanbeyan-east", "queanbeyan-west", "karabar", "jerrabomberra"],
        "scheduling": "Usually within the week for Queanbeyan",
    },
    {
        "name": "Queanbeyan East",
        "slug": "queanbeyan-east",
        "postcode": "2620",
        "region": "Queanbeyan",
        "hero_lead": "Queanbeyan East covers the established residential area east of the town centre — a mix of post-war homes, 1970s and 80s builds, and some newer infill development. The blocks are generally generous, the gardens are mature, and the suburb has a settled, family-oriented character. Close to the Queanbeyan CBD and the river, with good access back into Canberra.",
        "why_paragraph": "Queanbeyan East has a similar feel to Canberra's older Inner South suburbs — established gardens, big trees, and homeowners who care about how their property looks. The Queanbeyan River corridor runs nearby, and some properties deal with the extra moisture and vegetation that comes with being close to the waterway. We adapt our service to those conditions — managing damp-zone lawns and the extra leaf load from the riparian trees.",
        "job_title": "Queanbeyan East riverside property — moisture-adapted care",
        "job_description": "Property near the Queanbeyan River — back lawn stays damp longer than the front, with moss developing in the shaded corners near the rear fence. Mowed the front at standard height, raised the cut on the damp back section, treated the mossy areas, edged all paths, and cleared the river-blown debris from the fence line. Fortnightly visits adjusted for seasonal conditions.",
        "nearby": ["queanbeyan", "karabar", "jerrabomberra"],
        "scheduling": "Usually within the week for Queanbeyan East",
    },
    {
        "name": "Queanbeyan West",
        "slug": "queanbeyan-west",
        "postcode": "2620",
        "region": "Queanbeyan",
        "hero_lead": "Queanbeyan West sits on the Canberra side of Queanbeyan — the closest part of Queanbeyan to the ACT border and suburbs like Oaks Estate and Fyshwick. A mix of older residential properties and some newer development, with terrain that rises toward the west. A lot of residents here commute into Canberra daily and want their gardens handled by someone reliable while they're at work.",
        "why_paragraph": "Queanbeyan West is the easiest Queanbeyan suburb for us to reach — it's literally on our route when we're working the southern Canberra suburbs. That proximity means no travel premium, quick scheduling, and we can slot Queanbeyan West jobs into our existing Canberra rounds efficiently. Same service, same quality, and often the same day we're working just across the border.",
        "job_title": "Queanbeyan West — efficient cross-border service",
        "job_description": "Standard residential property in Queanbeyan West — mowed front and back lawns, edged all paths and the driveway, mowed the nature strip, trimmed the front hedge, and blew down all hard surfaces. Serviced on the same run as our Oaks Estate and Fyshwick customers — efficient routing means competitive pricing for Queanbeyan West.",
        "nearby": ["queanbeyan", "queanbeyan-east", "karabar"],
        "scheduling": "Usually within the week for Queanbeyan West",
    },
    {
        "name": "Karabar",
        "slug": "karabar",
        "postcode": "2620",
        "region": "Queanbeyan",
        "hero_lead": "Karabar is one of the larger Queanbeyan suburbs — spread across hilly terrain on the eastern side of town. Built primarily in the 1980s and 90s, it has a similar character to Canberra's Tuggeranong suburbs: family homes on decent blocks, established gardens, and a suburban infrastructure that's well-settled. The hills give some properties great views but also create real slope challenges.",
        "why_paragraph": "Karabar's hilly terrain means a lot of blocks have significant slope — similar to what we deal with in Fadden or Macarthur on the Canberra side. We know how to handle steep blocks safely and effectively: mowing across the slope, using line trimmers on the steep sections, and managing the soil erosion that gravity creates on the steeper garden beds. The battery gear helps — lighter and easier to handle on a gradient.",
        "job_title": "Karabar hillside block — slope-aware lawn service",
        "job_description": "Steeply sloping Karabar block — mowed the relatively flat front section normally, worked across the slope on the steep backyard, line-trimmed the steepest bank section where the mower can't safely go, edged all retaining wall tops, and cleared soil and debris that had washed down to the lower fence line after recent rain. Careful, methodical work on challenging terrain.",
        "nearby": ["queanbeyan", "queanbeyan-east", "jerrabomberra"],
        "scheduling": "Usually within the week for Karabar",
    },
    {
        "name": "Jerrabomberra",
        "slug": "jerrabomberra",
        "postcode": "2619",
        "region": "Queanbeyan",
        "hero_lead": "Jerrabomberra is the premium residential suburb in the Queanbeyan region — a planned estate development that started in the 1990s and expanded through the 2000s, with larger blocks, quality housing, and a strong community centred around the local shops, schools, and sporting facilities. It has a feel similar to Canberra's Nicholls or Forde — well-maintained, family-oriented, with higher presentation expectations.",
        "why_paragraph": "Jerrabomberra homeowners invest in their properties and expect a garden service that matches. The blocks are larger than newer Canberra suburbs, the gardens are well-established, and presentation matters on these streets. We bring the same premium service we deliver to Canberra's best suburbs — consistent quality, reliable scheduling, and results that keep these properties looking as good as they should.",
        "job_title": "Jerrabomberra premium property — full garden service",
        "job_description": "Large Jerrabomberra property — mowed the extensive front and rear lawns with a striped finish, edged all borders and the curved garden bed outlines, trimmed three separate hedges, weeded the feature planting beds in the front garden, pruned back the ornamental trees along the driveway, and blew down the double-car driveway and all paths. Two-hour visit for a property that gets the full treatment.",
        "nearby": ["karabar", "queanbeyan-east", "queanbeyan"],
        "scheduling": "Usually within the week for Jerrabomberra",
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
    print(f"\nGenerated {len(SUBURBS)} Queanbeyan suburb pages.")

if __name__ == "__main__":
    generate()
