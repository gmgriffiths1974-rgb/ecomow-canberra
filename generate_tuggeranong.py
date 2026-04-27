#!/usr/bin/env python3
"""Generate Tuggeranong suburb pages for EcoMow Canberra."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from generate_belconnen import TEMPLATE, REVIEWS

SUBURBS = [
    {
        "name": "Banks",
        "slug": "banks",
        "postcode": "2906",
        "region": "Tuggeranong",
        "hero_lead": "Banks is right down in Tuggeranong's southern pocket — one of the newer suburbs in the valley, built through the late 1990s. Smaller blocks compared to the older Tuggeranong suburbs, but tidy homes with front gardens that face the street and backyards that often look out toward the Lanyon landscape. Compact lawns that still need proper care.",
        "why_paragraph": "Banks' newer builds mean the soil profile is often still settling — a lot of clay base with thin topsoil, which affects drainage and lawn health. We see a lot of patchy couch lawns struggling in heavy clay here. We adjust our approach accordingly — higher mowing heights to protect root systems, and honest advice about top-dressing and soil improvement when it's needed.",
        "job_title": "Banks front and back — compact block full service",
        "job_description": "Standard residential block in Banks — mowed front and back lawns, edged all paths and the driveway, trimmed the small hedge along the front boundary, weeded the garden beds either side of the front door, and blew down all hard surfaces. Compact block, done properly in under an hour.",
        "nearby": ["gordon", "conder", "bonython"],
        "scheduling": "Usually within the week for Banks",
    },
    {
        "name": "Bonython",
        "slug": "bonython",
        "postcode": "2905",
        "region": "Tuggeranong",
        "hero_lead": "Bonython sits on the western side of Tuggeranong, running up the slope toward the Murrumbidgee River corridor. The suburb has a real mix — some larger blocks on the upper streets with views across the valley, and more typical-sized properties closer to Isabella Drive. The Bonython Primary School and neighbourhood oval are the heart of the community.",
        "why_paragraph": "Bonython's western slope means the blocks higher up get smashed by afternoon sun in summer and cop the westerly winds. Lawns on those exposed upper blocks dry out fast and need different management to the sheltered lower properties. We know which streets need what — and we're in Bonython regularly enough to time visits around the conditions.",
        "job_title": "Bonython upper block — exposed lawn recovery",
        "job_description": "Large corner block on Bonython's upper streets — lawn had thinned badly over summer on the north-facing section. Mowed the surviving turf at a higher setting, aerated the compacted areas along the driveway edge, and raked out the dead thatch from the worst patches. Recommended a top-dress and overseed in autumn. Regular fortnightly mow booked.",
        "nearby": ["banks", "gordon", "isabella-plains", "theodore"],
        "scheduling": "Usually within the week for Bonython",
    },
    {
        "name": "Calwell",
        "slug": "calwell",
        "postcode": "2905",
        "region": "Tuggeranong",
        "hero_lead": "Calwell is one of the mid-Tuggeranong suburbs with a well-established local centre — shops, schools, and the kind of mature streetscapes that come from being built in the late 1980s. Blocks vary from compact to generous, and the gardens have had thirty-plus years to fill out. Big hedges, shady backyards, and lawns that have seen a few different owners' attempts at improvement.",
        "why_paragraph": "Calwell's mature plantings mean a lot of shade management. Those thirty-year-old eucalypts and conifers that were saplings when the house was built now dominate entire backyards. We know how to work with heavy shade — adjusted mowing heights, managing moss and bare patches where grass can't compete, and keeping everything looking good even where the canopy means lawn was never going to thrive.",
        "job_title": "Calwell shaded backyard reclaim",
        "job_description": "Large backyard dominated by two mature eucalypts — mowed the sunny areas at standard height, raised the cut in the shaded zones, cleared accumulated bark and leaf debris from the beds, edged around all tree bases, and shaped the low hedge along the side boundary. Realistic conversation with the owner about shade-tolerant groundcover options for the bare patches.",
        "nearby": ["theodore", "richardson", "isabella-plains"],
        "scheduling": "Usually within the week for Calwell",
    },
    {
        "name": "Chisholm",
        "slug": "chisholm",
        "postcode": "2905",
        "region": "Tuggeranong",
        "hero_lead": "Chisholm is a well-connected Tuggeranong suburb sitting alongside the Tuggeranong Parkway — close to Erindale shops and the Hyperdome. Built primarily in the 1980s, it has good-sized blocks with established gardens, wide streets, and generous nature strips. A lot of families have been here for decades, and the gardens reflect that stability.",
        "why_paragraph": "Chisholm borders the Tuggeranong Parkway corridor, and properties along that edge tend to accumulate more dust and leaf debris than the interior streets. We see a lot of photinia and privet hedges along the parkway-side boundaries that need regular attention. The wide nature strips in Chisholm are part of the suburb's character — keeping them tidy lifts the whole street.",
        "job_title": "Chisholm parkway-side property cleanup",
        "job_description": "Property backing onto the Tuggeranong Parkway corridor — heavy leaf accumulation along the rear fence, gutters full of debris, and the nature strip hadn't been mowed in a while. Full cleanup: gutters cleared, rear fence line raked and blown clean, both nature strips mowed and edged, front and back lawns done, and all accumulated green waste bagged and removed.",
        "nearby": ["gilmore", "richardson", "fadden"],
        "scheduling": "Usually within the week for Chisholm",
    },
    {
        "name": "Conder",
        "slug": "conder",
        "postcode": "2906",
        "region": "Tuggeranong",
        "hero_lead": "Conder is one of the southernmost suburbs in Tuggeranong — a 1990s development that backs onto the hills and open grassland toward Lanyon. A lot of homes here have views, reasonable block sizes, and that slightly newer-build feeling with less established gardens than the older Tuggeranong suburbs. The Conder shops and Lanyon Marketplace are close by.",
        "why_paragraph": "Conder's position on the edge of Tuggeranong means more wind exposure and a slightly different microclimate to the valley-floor suburbs. The soil is often shallow and rocky on the upper blocks. We adjust for that — cutting higher where the turf is thin over rock, being careful with edging near shallow root systems, and managing the windblown debris that accumulates along fence lines.",
        "job_title": "Conder hilltop block — wind-exposed lawn care",
        "job_description": "Elevated corner block in upper Conder — front lawn mowed with the cut raised to protect the shallow turf, edged carefully around garden beds with rock borders, cleared windblown leaf debris from the garage side passage and rear fence line. Quick hedge trim on the front boundary. Clean, tidy result despite the challenging conditions.",
        "nearby": ["banks", "gordon", "lanyon"],
        "scheduling": "Usually within the week for Conder",
    },
    {
        "name": "Fadden",
        "slug": "fadden",
        "postcode": "2904",
        "region": "Tuggeranong",
        "hero_lead": "Fadden is tucked into the hillside between Gowrie and Macarthur — one of the hillier suburbs in Tuggeranong with some genuinely steep blocks and properties that terrace down the slope. The Mount Fadden Nature Reserve backs onto the eastern edge, giving a bushland feel to properties in that pocket. Good-sized blocks, mature gardens, and terrain that keeps you honest.",
        "why_paragraph": "Fadden's steep blocks are a real factor in how we work. Some backyards here drop several metres from the house to the rear fence — you can't just run a mower straight across. We work these blocks methodically, mowing across the slope where it's safe and using our battery line trimmer on the sections that are too steep for a mower. The battery gear matters here — lighter, quieter, and easier to handle on a gradient.",
        "job_title": "Fadden steep backyard — multi-level mow",
        "job_description": "Steeply terraced backyard with three distinct levels — mowed the upper lawn section with the push mower across the slope, line-trimmed the steep transition banks between levels, mowed the lower flat section, edged all retaining wall tops and paths, and cleared all clippings from the paved entertaining area at the bottom. Good workout.",
        "nearby": ["gowrie", "macarthur", "chisholm"],
        "scheduling": "Usually within the week for Fadden",
    },
    {
        "name": "Gilmore",
        "slug": "gilmore",
        "postcode": "2905",
        "region": "Tuggeranong",
        "hero_lead": "Gilmore is a compact mid-Tuggeranong suburb — built in the late 1980s with a consistent housing stock of mostly single-storey family homes on standard blocks. The Gilmore shops provide a quiet local centre, and the suburb has a settled, family-neighbourhood character. Neat streets, established gardens, and the kind of regular mowing work that suits a reliable schedule.",
        "why_paragraph": "Gilmore is one of those suburbs where consistency matters most. The blocks are similar sizes, the lawns are similar types, and most homeowners want the same thing — a reliable, tidy result on a regular schedule. We've got a good concentration of regular customers in Gilmore, which means we're there every fortnight rain or hail. Your street probably already has someone we mow for.",
        "job_title": "Gilmore fortnightly regular — front, back and verge",
        "job_description": "Standard Gilmore fortnightly visit — mowed front and back lawns, edged along all paths and the driveway, mowed both nature strips, blew down the driveway and front path. Twelve minutes start to finish. Regular customers get priority scheduling and consistent pricing — no surprises.",
        "nearby": ["chisholm", "richardson", "isabella-plains"],
        "scheduling": "Usually within the week for Gilmore",
    },
    {
        "name": "Gordon",
        "slug": "gordon",
        "postcode": "2906",
        "region": "Tuggeranong",
        "hero_lead": "Gordon is the southernmost suburb in Canberra — right on the edge where the city gives way to rural land. It's a 1990s development with a newer, modern housing stock and a different feel to the older Tuggeranong suburbs. Gordon has its own local shops, good community facilities, and blocks that are generally a bit smaller than the older valley suburbs but well-designed.",
        "why_paragraph": "Gordon's proximity to rural land means the frost line hits harder and earlier than suburbs further into the valley. Winter mornings in Gordon can be brutal on warm-season grasses — we see more frost damage here than almost anywhere else in our service area. We time our winter visits for later in the morning when the frost has lifted, and adjust our advice about grass varieties accordingly.",
        "job_title": "Gordon frost-recovery lawn care",
        "job_description": "Front lawn showing heavy frost damage from an extended cold snap — brown and dormant couch grass across most of the block. Mowed at maximum height to avoid stressing the crowns, cleaned up the dead leaf matter that had accumulated, edged neatly, and advised the owner to hold off on any treatment until the grass starts actively growing again in September.",
        "nearby": ["banks", "conder", "bonython"],
        "scheduling": "Usually within the week for Gordon",
    },
    {
        "name": "Gowrie",
        "slug": "gowrie",
        "postcode": "2904",
        "region": "Tuggeranong",
        "hero_lead": "Gowrie sits in the middle of Tuggeranong — a solid 1980s suburb with the Erindale Centre right on its doorstep. The suburb is on gently undulating terrain with a mix of single-storey homes and some dual-occupancy developments that have appeared in recent years. The mature street trees give Gowrie a green, established look, and most blocks have well-developed gardens.",
        "why_paragraph": "Gowrie's central position in the Tuggeranong valley means it's one of our most efficient suburbs to service — we're often passing through on the way to other jobs. That accessibility means we can slot in Gowrie visits easily, keep response times short, and schedule reliably. A lot of our Gowrie customers have been with us for years because the service is consistent and we never skip a visit.",
        "job_title": "Gowrie dual-occ front yard pair",
        "job_description": "Dual-occupancy property in Gowrie — both units serviced in a single visit. Mowed the shared front lawn area, edged the common driveway, trimmed the low dividing hedge between the two units, blew down both front paths and the shared carpark area. Both tenants happy, body corporate invoiced as one job.",
        "nearby": ["fadden", "oxley", "erindale"],
        "scheduling": "Usually within the week for Gowrie",
    },
    {
        "name": "Greenway",
        "slug": "greenway",
        "postcode": "2900",
        "region": "Tuggeranong",
        "hero_lead": "Greenway is the town centre of Tuggeranong — home to the Tuggeranong Hyperdome, the lake foreshore, government offices, and the highest concentration of medium-density housing in the valley. A lot of the residential properties here are townhouses, apartments, and units rather than standalone houses. Strata and body corporate work is a big part of what we do in Greenway.",
        "why_paragraph": "Greenway's medium-density character means a lot of our work here is for body corporates and strata managers — common area mowing, shared hedge trimming, entrance garden maintenance. We carry all the insurance documentation that strata managers need, invoice cleanly, and deliver consistent results that keep residents happy and managers off the phone.",
        "job_title": "Greenway townhouse complex — common area service",
        "job_description": "Twelve-unit townhouse complex in Greenway — mowed all common lawn areas, edged along all shared paths, trimmed hedges at the front entrance and along the visitor carpark, cleared leaves from the common courtyard, and blew down all hard surfaces. Monthly schedule, strata manager invoiced directly. Professional photos sent with the invoice.",
        "nearby": ["oxley", "wanniassa", "kambah"],
        "scheduling": "Usually within the week for Greenway",
    },
    {
        "name": "Isabella Plains",
        "slug": "isabella-plains",
        "postcode": "2905",
        "region": "Tuggeranong",
        "hero_lead": "Isabella Plains is a late-1980s suburb in the southern part of Tuggeranong — wider streets, good-sized blocks, and a layout that feels more spacious than some of the newer developments. The Calwell shops are just next door, and the suburb has that settled, established-family character with big trees and gardens that have had decades to mature.",
        "why_paragraph": "Isabella Plains has some of the bigger residential blocks in southern Tuggeranong, and a lot of homeowners here have invested in their gardens over the years. We see substantial hedges, multiple garden beds, fruit trees, and lawns that need proper seasonal management. This is the kind of suburb where a full garden maintenance service — not just a mow — really makes sense.",
        "job_title": "Isabella Plains full garden maintenance visit",
        "job_description": "Comprehensive monthly maintenance visit — mowed front and back lawns, edged all borders, pruned back the overgrown rosemary along the side fence, trimmed the front hedge, weeded three garden beds, removed dead stems from the perennial border, and cleared all debris from paths and the patio. A proper garden service, not just a drive-by mow.",
        "nearby": ["calwell", "bonython", "gilmore", "theodore"],
        "scheduling": "Usually within the week for Isabella Plains",
    },
    {
        "name": "Kambah",
        "slug": "kambah",
        "postcode": "2902",
        "region": "Tuggeranong",
        "hero_lead": "Kambah is Tuggeranong's biggest suburb by area and population — it stretches from the Murrumbidgee corridor in the west across to the Tuggeranong Parkway in the east. Built from the late 1970s, Kambah has enormous variety: big blocks on the western ridge, standard suburban lots in the middle, and some newer infill development throughout. It's practically a town in itself.",
        "why_paragraph": "Kambah is big enough that conditions change meaningfully across the suburb. The western blocks near the Murrumbidgee are exposed, windy, and frost-prone. The central streets are sheltered and warm. The eastern edge near the Parkway collects road dust and noise. We service all of it regularly and know the micro-conditions across Kambah's different pockets — your lawn gets treated based on where it actually is, not a generic suburb-wide assumption.",
        "job_title": "Kambah large block — western ridge full service",
        "job_description": "Oversized block on Kambah's western ridge — front lawn, large backyard, two side passages, and an extensive nature strip all mowed and edged. Trimmed the boundary hedge along the west fence, cleared wind-deposited leaf debris from behind the shed, and blew down the long driveway. Big job, but we price fairly for the actual time and effort.",
        "nearby": ["wanniassa", "greenway", "oxley"],
        "scheduling": "Usually within the week for Kambah",
    },
    {
        "name": "Macarthur",
        "slug": "macarthur",
        "postcode": "2904",
        "region": "Tuggeranong",
        "hero_lead": "Macarthur is a smaller suburb on the eastern side of Tuggeranong — perched up on the hillside with some of the best views in the valley. It's an older 1980s development with generous blocks, well-established gardens, and a quiet, tucked-away feeling despite being close to Fadden and Gowrie. The Macarthur ridge gives the suburb its character and its challenges.",
        "why_paragraph": "Macarthur's elevated position means rocky, shallow soils on a lot of blocks and serious slope on some properties. The views are great, but the terrain demands more from a lawn care perspective. We bring the right approach — appropriate mowing heights for thin-soil turf, careful edging around rock outcrops, and realistic conversations about what will and won't thrive in those conditions.",
        "job_title": "Macarthur ridge block — rocky terrain lawn service",
        "job_description": "Elevated block on the Macarthur ridge — front lawn mowed carefully around exposed rock and shallow soil areas, back lawn done at raised height where turf is thin, edged all paths, trimmed the native hedge along the front boundary, and cleared accumulated bark debris from the side passage. Blade inspection after the job — rocky blocks are tough on gear.",
        "nearby": ["fadden", "gowrie", "gilmore"],
        "scheduling": "Usually within the week for Macarthur",
    },
    {
        "name": "Monash",
        "slug": "monash",
        "postcode": "2904",
        "region": "Tuggeranong",
        "hero_lead": "Monash is a well-regarded suburb on Tuggeranong's northern rim — a 1980s development with a strong community centred around the Monash shops, good schools, and the wide, tree-lined streets that give the suburb a premium feel. Blocks are generous, gardens are well-maintained, and there's a pride-of-place attitude among homeowners that lifts the whole suburb.",
        "why_paragraph": "Monash homeowners generally keep their properties to a high standard, and they expect the same from their lawn care provider. We deliver that — clean lines, consistent mowing heights, neat edging, and no shortcuts. A lot of our Monash customers initially came to us because their previous mower was inconsistent. We show up when we say we will, every time.",
        "job_title": "Monash premium front — show-home standard",
        "job_description": "Well-maintained Monash property where presentation matters — front lawn mowed in alternating directions for a striped finish, all edges cut with a string line, the formal front hedge trimmed to a crisp box shape, garden beds weeded and mulch raked even, and all clippings and debris removed completely. The kind of result that makes the neighbours reconsider their current mower.",
        "nearby": ["oxley", "fadden", "wanniassa"],
        "scheduling": "Usually within the week for Monash",
    },
    {
        "name": "Oxley",
        "slug": "oxley",
        "postcode": "2903",
        "region": "Tuggeranong",
        "hero_lead": "Oxley is a small suburb on the shores of Lake Tuggeranong — one of the more premium pockets in the valley, with some properties offering direct lake views or backing onto the foreshore parkland. Built in the early 1980s, the gardens are fully mature, the blocks are generous, and the suburb has a quiet, established character.",
        "why_paragraph": "Oxley's proximity to the lake creates a slightly milder microclimate than the hilltop suburbs — less frost, more moisture, and lawns that tend to stay greener through winter. But it also means more work managing moisture-related issues in the cooler months — moss in shaded areas, mushroom rings in autumn, and lawns that stay damp longer after rain. We manage all of it.",
        "job_title": "Oxley lakeside garden maintenance",
        "job_description": "Large block backing onto the Lake Tuggeranong foreshore — mowed the expansive front and back lawns, treated a persistent moss patch in the shaded rear corner with an iron sulphate application, edged all garden beds and paths, trimmed the side boundary hedge, and cleared lake-blown debris from the back fence line. Beautiful property, deserves the attention.",
        "nearby": ["greenway", "gowrie", "monash", "wanniassa"],
        "scheduling": "Usually within the week for Oxley",
    },
    {
        "name": "Richardson",
        "slug": "richardson",
        "postcode": "2905",
        "region": "Tuggeranong",
        "hero_lead": "Richardson is a compact mid-Tuggeranong suburb with a strong community feel — the Richardson shops, a good local school, and well-kept streets give it a settled, family-friendly character. Built in the 1980s, the blocks are mostly standard residential size with established gardens and mature street trees that create a green, shady canopy along the main roads.",
        "why_paragraph": "Richardson's tree-lined streets mean a lot of the front gardens deal with significant leaf drop, especially in autumn. The big deciduous street trees dump leaves across nature strips and front lawns for weeks. We factor seasonal leaf clearing into our regular mowing visits — no point mowing around a carpet of leaves. The whole frontage gets cleared as part of the service.",
        "job_title": "Richardson autumn leaf and mow combination",
        "job_description": "Regular fortnightly visit during peak autumn leaf drop — cleared heavy leaf accumulation from the front lawn and nature strip using the battery blower, mowed the front and back lawns once cleared, edged all paths, and bagged the collected leaves for removal. Three full bags of elm leaves from a single visit. Part of the regular service, no extra charge.",
        "nearby": ["chisholm", "gilmore", "calwell"],
        "scheduling": "Usually within the week for Richardson",
    },
    {
        "name": "Theodore",
        "slug": "theodore",
        "postcode": "2905",
        "region": "Tuggeranong",
        "hero_lead": "Theodore is a late-1980s suburb in Tuggeranong's southern corridor — named after a former PM and sitting between Calwell and Bonython with the Murrumbidgee corridor to the west. Reasonable block sizes, a local primary school, and the kind of suburban fabric where families put down roots. Some blocks on the western edge have views to the river corridor and the hills beyond.",
        "why_paragraph": "Theodore's western blocks near the Murrumbidgee corridor deal with real bushfire interface conditions — long grass on the reserve boundary, leaf accumulation against fences, and overhanging branches. We help Theodore homeowners maintain their Asset Protection Zone properly — mowing to the boundary, clearing debris from fence lines, and keeping the defensible space around the house in good order heading into summer.",
        "job_title": "Theodore bushfire-edge property preparation",
        "job_description": "Western-edge Theodore property backing onto the Murrumbidgee corridor — mowed the full block with an emphasis on the reserve boundary strip, cleared all leaf litter and debris from the rear and side fence lines, trimmed overhanging branches within reach, cleaned the gutters, and mowed the nature strip. Pre-summer fire prep done right.",
        "nearby": ["calwell", "bonython", "isabella-plains"],
        "scheduling": "Usually within the week for Theodore",
    },
    {
        "name": "Wanniassa",
        "slug": "wanniassa",
        "postcode": "2903",
        "region": "Tuggeranong",
        "hero_lead": "Wanniassa is one of Tuggeranong's original suburbs — established in the late 1970s with the kind of big blocks, mature trees, and wide streets that the newer suburbs can only dream about. It sits right in the heart of the valley with the Erindale Centre nearby, good schools, and a suburban character that's had almost fifty years to develop. These are properly established gardens.",
        "why_paragraph": "Wanniassa's age means the gardens are fully mature — and in some cases overgrown. We do a lot of garden reclamation work here, bringing overgrown properties back to a manageable state. It's also one of our highest-density suburbs for regular fortnightly customers. We're in Wanniassa almost every day of the working week, which means quick scheduling and no travel premium.",
        "job_title": "Wanniassa overgrown garden reclamation",
        "job_description": "Property that had been let go for about six months — grass knee-high front and back, hedges grown well out of shape, garden beds invisible under weeds. Two-visit job: first pass to knock everything back to manageable height and shape, second visit a fortnight later to refine the cut and establish a clean baseline. Property went from embarrassment to respectable in two visits. Now on a regular fortnightly schedule.",
        "nearby": ["kambah", "greenway", "oxley", "monash"],
        "scheduling": "Usually within the week for Wanniassa",
    },
]

def generate():
    base = os.path.dirname(os.path.abspath(__file__))
    suburbs_dir = os.path.join(base, "suburbs")
    # Build a name lookup from all suburbs in this file
    name_map = {s["slug"]: s["name"] for s in SUBURBS}
    # Add cross-references to other regions
    name_map.update({
        "curtin":"Curtin", "erindale":"Erindale", "lanyon":"Lanyon",
        "chapman":"Chapman", "fisher":"Fisher", "stirling":"Stirling",
    })
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
    print(f"\nGenerated {len(SUBURBS)} Tuggeranong suburb pages.")

if __name__ == "__main__":
    generate()
