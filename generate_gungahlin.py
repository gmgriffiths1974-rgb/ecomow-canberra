#!/usr/bin/env python3
"""Generate Gungahlin suburb pages for EcoMow Canberra."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from generate_belconnen import TEMPLATE, REVIEWS

SUBURBS = [
    {
        "name": "Amaroo",
        "slug": "amaroo",
        "postcode": "2914",
        "region": "Gungahlin",
        "hero_lead": "Amaroo is one of Gungahlin's earlier established suburbs — built from the early 2000s with a real community feel centred around the Amaroo shops and the local school. The blocks here are a bit more generous than the newer Gungahlin developments, and the gardens have had two decades to establish. Mature street trees, filled-out hedges, and lawns that are properly settled.",
        "why_paragraph": "Amaroo's slightly older stock means the gardens are established enough to need proper maintenance rather than just a quick mow. We see a lot of well-developed hedges, fruit trees, and garden beds that need seasonal attention alongside the regular lawn care. Amaroo homeowners tend to take pride in their properties, and we match that with a thorough, consistent service.",
        "job_title": "Amaroo established garden — full seasonal service",
        "job_description": "Quarterly seasonal maintenance visit — mowed front and back, edged all borders, pruned the fruit trees along the back fence, shaped the front hedge, weeded all garden beds, cut back spent perennials, and raked the mulch in the feature bed out front. Comprehensive garden care, not just lawn mowing.",
        "nearby": ["bonner", "forde", "harrison"],
        "scheduling": "Usually within the week for Amaroo",
    },
    {
        "name": "Bonner",
        "slug": "bonner",
        "postcode": "2914",
        "region": "Gungahlin",
        "hero_lead": "Bonner is out on Gungahlin's northern fringe — a newer suburb that was still being developed into the 2010s. It has a modern, planned feel with wide streets, good parks, and blocks that range from compact townhouse lots to reasonable standalone properties. A lot of young families bought here, and the gardens are still relatively new and developing.",
        "why_paragraph": "Bonner's newer gardens mean a lot of the turf is still establishing, and some of the builder-installed lawns were done to a budget standard — thin topsoil over heavy clay, instant turf that wasn't prepared properly. We help Bonner homeowners get the best out of what they've got, and give honest advice about soil improvement and turf health when the original install wasn't great.",
        "job_title": "Bonner new-build lawn establishment",
        "job_description": "Relatively new property where the builder's turf had thinned badly — mowed the surviving areas at maximum height to protect the crowns, top-dressed the bare patches with a compost and soil blend, overseeded with a couch variety to match the existing turf, and set up a fortnightly maintenance schedule. Six weeks later the lawn looked completely different.",
        "nearby": ["amaroo", "forde", "jacka"],
        "scheduling": "Usually within the week for Bonner",
    },
    {
        "name": "Casey",
        "slug": "casey",
        "postcode": "2913",
        "region": "Gungahlin",
        "hero_lead": "Casey is one of Gungahlin's larger suburbs — a 2000s development spread across rolling terrain on the eastern side of the district. It has multiple pocket parks, the Casey shops, and a mix of housing from standalone family homes to townhouse clusters. The suburb's terrain varies from flat to gently undulating, and the open grassland around the edges gives it a semi-rural feel in places.",
        "why_paragraph": "Casey's size means conditions vary across the suburb — the lower sections near the drainage corridors stay damper, while the exposed hilltop blocks dry out quickly in summer. We service a lot of Casey properties on a regular basis and know which pockets need different treatment. Your lawn gets managed based on its actual conditions, not a one-size-fits-all approach.",
        "job_title": "Casey drainage corridor property — damp-zone lawn management",
        "job_description": "Property adjacent to a Casey drainage swale — the back lawn stays damp well after rain and had developed moss and compaction issues. Mowed at standard height on the dry sections, raised the cut on the damp rear zone, scarified the mossy areas, and applied a light top-dress of sand to improve surface drainage. Regular fortnightly mow with seasonal moss treatment.",
        "nearby": ["ngunnawal", "nicholls", "taylor"],
        "scheduling": "Usually within the week for Casey",
    },
    {
        "name": "Crace",
        "slug": "crace",
        "postcode": "2911",
        "region": "Gungahlin",
        "hero_lead": "Crace is a compact suburb on Gungahlin's southern edge — close to the city, well-connected, and with a distinctive design that mixes traditional housing with medium-density development around the Crace shops. The suburb backs onto the Crace Nature Reserve, giving properties along that boundary a bushland outlook and some interesting garden challenges.",
        "why_paragraph": "Crace's proximity to the nature reserve means properties on the eastern edge deal with kangaroo traffic, native seed germination in garden beds, and a different soil profile to the newer developed areas. We know how to manage the bush interface — keeping the garden looking intentional rather than letting the reserve creep in, while being respectful of the native vegetation that gives Crace its character.",
        "job_title": "Crace reserve-edge garden management",
        "job_description": "Property backing onto Crace Nature Reserve — mowed front and back lawns, removed native grass seedlings that had germinated through the back garden beds, repaired two patches of kangaroo damage in the back lawn with a rake and overseed, trimmed the boundary hedge, and maintained clear separation between the garden and the reserve margin. Monthly visits scheduled.",
        "nearby": ["palmerston", "mitchell", "franklin"],
        "scheduling": "Usually within the week for Crace",
    },
    {
        "name": "Forde",
        "slug": "forde",
        "postcode": "2914",
        "region": "Gungahlin",
        "hero_lead": "Forde is a premium pocket in northern Gungahlin — a well-designed suburb with a mix of quality standalone homes and townhouses, good green spaces, and the Mulligans Flat Nature Reserve right on the doorstep. The blocks are generally well-proportioned, and the suburb has matured nicely since it was developed in the late 2000s. A lot of owner-occupiers who care about presentation.",
        "why_paragraph": "Forde attracts homeowners who want their properties looking sharp, and the proximity to Mulligans Flat means the local wildlife is a regular garden visitor. Wallabies, kangaroos, and native birds are part of the deal here. We work with that reality — knowing which plants the roos leave alone, how to repair wallaby grazing damage, and maintaining gardens that look great despite the wildlife pressure.",
        "job_title": "Forde premium property — presentation-focused service",
        "job_description": "Well-presented Forde home — mowed in alternating directions for stripe finish, precision-edged all borders, trimmed the formal front hedge to a crisp line, weeded the feature garden beds, spot-treated two patches of wallaby grazing damage in the back lawn, and blew down the driveway and entrance path. Presentation-grade result.",
        "nearby": ["bonner", "amaroo", "taylor"],
        "scheduling": "Usually within the week for Forde",
    },
    {
        "name": "Franklin",
        "slug": "franklin",
        "postcode": "2913",
        "region": "Gungahlin",
        "hero_lead": "Franklin is a well-established Gungahlin suburb sitting right alongside the light rail corridor — one of the suburbs that benefited most from Canberra's light rail investment. The housing stock is a mix of family homes and medium-density development, with the Franklin shops providing a genuine village centre. Good parks, established gardens, and strong community infrastructure.",
        "why_paragraph": "Franklin's light rail access has made it one of the more sought-after Gungahlin suburbs, and property presentation reflects that. A lot of our Franklin customers are families who want their property looking its best — regular mowing, tidy edges, and gardens that present well from the street. We deliver that consistently, and the efficient access via Gungahlin Drive means we're in Franklin on schedule every time.",
        "job_title": "Franklin family home — regular fortnightly maintenance",
        "job_description": "Standard Franklin family home on a fortnightly schedule — mowed the front, side, and back lawns, edged along all paths and the driveway, mowed both nature strips, trimmed the low front fence hedge, and blew down all hard surfaces. Consistent result every two weeks, rain or shine. Priority scheduling for regular customers.",
        "nearby": ["harrison", "gungahlin", "crace"],
        "scheduling": "Usually within the week for Franklin",
    },
    {
        "name": "Gungahlin",
        "slug": "gungahlin",
        "postcode": "2912",
        "region": "Gungahlin",
        "hero_lead": "Gungahlin town centre is the hub of the district — shops, restaurants, the light rail terminus, government offices, and a high concentration of medium-density residential development. Townhouses, apartments, and unit complexes are the dominant residential form here, which means a lot of our work in Gungahlin is strata and body corporate maintenance.",
        "why_paragraph": "Gungahlin's town centre character means we're mostly working on common areas, shared gardens, and body corporate properties here. We carry full public liability documentation, invoice directly to strata managers or body corporate committees, and provide the kind of reliable, documented service that keeps everyone happy — residents, managers, and committee members.",
        "job_title": "Gungahlin apartment complex — quarterly grounds maintenance",
        "job_description": "Twenty-four-unit apartment complex in Gungahlin — all common lawns mowed, entrance hedges trimmed, garden beds weeded and mulch topped up, courtyard areas cleared, bin enclosure tidied, and visitor carpark edges edged. Quarterly deep-maintenance visit supplementing the fortnightly mow. Full photo report provided to the body corporate manager.",
        "nearby": ["franklin", "harrison", "palmerston"],
        "scheduling": "Usually within the week for Gungahlin",
    },
    {
        "name": "Harrison",
        "slug": "harrison",
        "postcode": "2914",
        "region": "Gungahlin",
        "hero_lead": "Harrison is one of Gungahlin's larger and more established suburbs — built from the early 2000s with a strong community centred around Harrison School, the local shops, and good sporting facilities. The blocks are generally a bit more generous than the newer Gungahlin suburbs, and the mix of housing ranges from family homes to townhouse clusters. Well-treed streets and settled gardens.",
        "why_paragraph": "Harrison's maturity within the Gungahlin context means the gardens are established and the homeowners have settled into their maintenance routines. We have a strong base of regular customers in Harrison — some who've been with us since we started — and the concentration means we're in the suburb almost daily. Quick turnaround on new bookings because we're always nearby.",
        "job_title": "Harrison long-term customer — fortnightly regular",
        "job_description": "One of our original Harrison customers — fortnightly mow and edge, front and back. This property gets the consistency that comes from the same team knowing the garden intimately: we know where the drainage dip is, where the tree roots lift the mower, and exactly how the owner likes the front hedge shaped. That's the value of a long-term relationship.",
        "nearby": ["franklin", "gungahlin", "amaroo"],
        "scheduling": "Usually within the week for Harrison",
    },
    {
        "name": "Jacka",
        "slug": "jacka",
        "postcode": "2914",
        "region": "Gungahlin",
        "hero_lead": "Jacka is one of the newest suburbs in Gungahlin — still being developed on the district's northern edge. A lot of new builds, fresh landscaping, and young families moving in. The blocks tend to be smaller than the older Gungahlin suburbs, following the modern compact-living trend, but the homes are modern and the gardens are starting from scratch.",
        "why_paragraph": "Jacka's brand-new gardens need a different approach to established suburbs. Fresh turf needs careful management in the first year — the right mowing height, not too short too soon, and honest advice about watering and fertilising to help it establish. We see a lot of Jacka homeowners frustrated with builder-grade turf that wasn't installed well. We help them get it right rather than just mowing whatever's there.",
        "job_title": "Jacka new-build — first-year turf management",
        "job_description": "New home in Jacka with turf installed three months ago — first professional mow at a conservative height to encourage root establishment, light edge along the new concrete paths, cleared construction debris from the side passage, and gave the owner a seasonal care guide for the first twelve months. Set up fortnightly visits to keep it on track.",
        "nearby": ["bonner", "taylor", "moncrieff"],
        "scheduling": "Usually within the week for Jacka",
    },
    {
        "name": "Mitchell",
        "slug": "mitchell",
        "postcode": "2911",
        "region": "Gungahlin",
        "hero_lead": "Mitchell is primarily known as Gungahlin's industrial and commercial precinct — but it also has a pocket of residential properties, particularly on its southern edge near the Crace border. The residential areas are mostly medium-density, and the commercial premises often need grounds maintenance too. It's a different type of work to the typical suburban lawn run.",
        "why_paragraph": "Mitchell's commercial character means a lot of our work here is maintaining the grounds and garden areas of businesses — office frontages, warehouse surrounds, car park edges, and common areas in commercial complexes. We bring the same quality to commercial work that we do to residential, and the professional presentation helps businesses make a good impression on their customers and staff.",
        "job_title": "Mitchell commercial premises — grounds maintenance",
        "job_description": "Commercial office property in Mitchell — mowed the front lawn area, edged along the customer carpark, trimmed the entrance hedges, weeded the garden beds either side of the front door, and blew down the footpath and carpark entrance. Monthly schedule, invoiced to the business. Clean, professional result that reflects well on the business.",
        "nearby": ["crace", "gungahlin", "franklin"],
        "scheduling": "Usually within the week for Mitchell",
    },
    {
        "name": "Moncrieff",
        "slug": "moncrieff",
        "postcode": "2914",
        "region": "Gungahlin",
        "hero_lead": "Moncrieff is a relatively new suburb in Gungahlin's north — developed through the 2010s with modern housing, good parks, and the Moncrieff Community Recreation Park as its centrepiece. The blocks are typical of newer Canberra — compact but well-designed, with smaller front yards and modest backyards. The community is young and growing, and the gardens are still establishing.",
        "why_paragraph": "Moncrieff's compact blocks mean the mowing itself is quick, but the detail matters more — when the whole front yard is visible from the street, a rough edge or missed strip is obvious. We bring precision to even the smallest blocks. And because the gardens are still young, we give honest advice about plant choices, turf care, and how to make a small garden look great rather than just small.",
        "job_title": "Moncrieff compact block — detail-focused service",
        "job_description": "Compact Moncrieff property — small front lawn mowed with clean stripes, precision-edged along the path and driveway, narrow side passage line-trimmed, back lawn mowed, low front hedge clipped, and all hard surfaces blown clean. Small block, but the detail makes it. Done in thirty minutes, priced fairly for the compact size.",
        "nearby": ["jacka", "amaroo", "casey"],
        "scheduling": "Usually within the week for Moncrieff",
    },
    {
        "name": "Ngunnawal",
        "slug": "ngunnawal",
        "postcode": "2913",
        "region": "Gungahlin",
        "hero_lead": "Ngunnawal is one of Gungahlin's original suburbs — built from the mid-1990s and now one of the most established and populated suburbs in the district. Large by area, varied in housing stock, and with a strong community identity built around the schools, shops, and sporting facilities. The gardens here have had twenty-plus years to mature, and the suburb feels settled and comfortable.",
        "why_paragraph": "Ngunnawal is a big suburb with a lot of variety — from original 1990s homes with large established gardens to newer infill townhouse developments. We service all of it and have one of our highest concentrations of regular customers here. The suburb's size means we can often schedule multiple jobs on the same street or in the same pocket, which keeps our efficiency high and your wait times short.",
        "job_title": "Ngunnawal street run — four properties in sequence",
        "job_description": "Four neighbouring Ngunnawal properties serviced back-to-back in a single morning — all front and back lawns mowed, all edges done, all nature strips included, one hedge trimmed, and one set of gutters cleared. Neighbours coordinating bookings through us means better prices, consistent timing, and a whole section of street looking sharp at once.",
        "nearby": ["casey", "nicholls", "palmerston"],
        "scheduling": "Usually within the week for Ngunnawal",
    },
    {
        "name": "Nicholls",
        "slug": "nicholls",
        "postcode": "2913",
        "region": "Gungahlin",
        "hero_lead": "Nicholls is one of Gungahlin's premium suburbs — established in the mid-1990s with larger blocks, generous setbacks, and a reputation for well-maintained properties. The Gold Creek village and its surroundings give the suburb a semi-rural character in places, and the housing quality reflects the suburb's position at the top of the Gungahlin market.",
        "why_paragraph": "Nicholls homeowners expect a high standard, and the larger blocks demand more time and attention than compact newer suburbs. We allocate the time these properties deserve — proper mowing patterns, thorough edging, careful hedge work, and a finish that justifies the premium blocks these homes sit on. Several of our longest-standing regular customers are in Nicholls.",
        "job_title": "Nicholls large block — premium full-service visit",
        "job_description": "Large Nicholls property on the Gold Creek side — expansive front lawn mowed with a professional striped finish, side and back lawns done to the same standard, three separate hedges trimmed, all garden bed edges cleaned, feature planting beds weeded, and the long driveway and paths blown spotless. Two-hour job for a property that deserves every minute of it.",
        "nearby": ["casey", "ngunnawal", "palmerston"],
        "scheduling": "Usually within the week for Nicholls",
    },
    {
        "name": "Palmerston",
        "slug": "palmerston",
        "postcode": "2913",
        "region": "Gungahlin",
        "hero_lead": "Palmerston is one of Gungahlin's founding suburbs — established in the early 1990s and now thoroughly mature. The blocks are generous by current standards, the trees are tall, the gardens are full, and the suburb has the kind of settled character that the newer Gungahlin suburbs are still building toward. Close to the Gungahlin town centre but with a distinctly suburban feel.",
        "why_paragraph": "Palmerston's maturity means the gardens need more than just mowing — thirty-year-old hedges need proper reshaping, established trees need clearance pruning, and the original garden beds need seasonal maintenance to keep looking intentional rather than overgrown. We offer the full range of garden services that Palmerston properties need, not just a quick mow and go.",
        "job_title": "Palmerston mature garden — comprehensive maintenance",
        "job_description": "Long-established Palmerston property — mowed front and back at differentiated heights for sun and shade, reshaped the overgrown front hedge that had lost its form over several seasons, pruned the ornamental pear to clear the path, weeded and mulched the front garden bed, and edged all borders. The kind of comprehensive service that brings a mature garden back to its best.",
        "nearby": ["ngunnawal", "gungahlin", "crace", "mitchell"],
        "scheduling": "Usually within the week for Palmerston",
    },
    {
        "name": "Taylor",
        "slug": "taylor",
        "postcode": "2913",
        "region": "Gungahlin",
        "hero_lead": "Taylor is one of the newest suburbs in Canberra — still actively being developed on Gungahlin's northern edge with new homes going up regularly. Modern designs, compact blocks, and a lot of young families settling in. The suburb is fresh, the gardens are brand new, and the community is just starting to take shape. Great time to get a regular maintenance routine locked in.",
        "why_paragraph": "Taylor's ongoing development means we're often working on properties where the house next door is still being built — dust from construction sites, builder's debris blowing onto freshly laid turf, and gardens that need extra attention in their first year. We help Taylor homeowners establish their gardens properly from day one, which saves money and frustration in the long run.",
        "job_title": "Taylor brand-new property — garden establishment support",
        "job_description": "Brand-new Taylor home with turf and landscaping just completed — first professional mow at a gentle height, cleared construction dust and debris from the garden beds, hand-weeded the new planting beds, installed garden edge along the lawn-to-bed border, and provided a first-year care plan. Monthly visits locked in while the garden establishes.",
        "nearby": ["jacka", "forde", "casey"],
        "scheduling": "Usually within the week for Taylor",
    },
]

def generate():
    base = os.path.dirname(os.path.abspath(__file__))
    suburbs_dir = os.path.join(base, "suburbs")
    name_map = {s["slug"]: s["name"] for s in SUBURBS}
    # Cross-region references
    name_map.update({"palmerston":"Palmerston", "mitchell":"Mitchell"})
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
    print(f"\nGenerated {len(SUBURBS)} Gungahlin suburb pages.")

if __name__ == "__main__":
    generate()
