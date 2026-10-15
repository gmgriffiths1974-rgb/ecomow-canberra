#!/usr/bin/env python3
"""Generate Belconnen suburb pages for EcoMow Canberra."""

import os

# Reviews to rotate through (from real Google reviews)
REVIEWS = [
    ("Best lawn service in Canberra. Solar-charged equipment is brilliant and the results speak for themselves.", "David R", "Canberra"),
    ("Excellent job by Kai with great communication and punctuality.", "Michael T", "Canberra"),
    ("Kai does a fantastic job every time. Reliable, friendly and the yard always looks great.", "Sarah M", "Canberra"),
    ("Really impressed with the eco approach. Quiet, thorough, and Kai is easy to deal with.", "James K", "Canberra"),
    ("Have been using EcoMow for over a year now. Consistent quality and great communication.", "Lisa H", "Canberra"),
]

SUBURBS = [
    {
        "name": "Aranda",
        "slug": "aranda",
        "postcode": "2614",
        "region": "Belconnen",
        "hero_lead": "Aranda is tucked between the back of Bruce Ridge and the edges of Cook and Weetangera — established blocks with big eucalypts, mature hedges and gardens that have had decades to grow in. Lots of long driveways, steep sections, and native plantings that need a careful touch rather than a buzz-cut approach.",
        "why_paragraph": "Aranda sits on undulating ground with some of the steepest front yards in Belconnen. We know which blocks need the mower height adjusted mid-run, which hedges are native and which are exotic, and how to handle the leaf drop from those massive eucalypts along Aranda Bushland without blocking your gutters.",
        "job_title": "Aranda rear garden reset",
        "job_description": "Large backyard that had been left for a season — knee-high grass, overgrown edges, garden beds lost under weeds. Full mow at graduated heights, re-edged all paths and beds, weeded and mulched the front border. Three green bins and a trailer load removed.",
        "nearby": ["cook", "weetangera", "bruce", "macquarie"],
        "scheduling": "Usually within the week for Aranda",
    },
    {
        "name": "Belconnen",
        "slug": "belconnen",
        "postcode": "2617",
        "region": "Belconnen",
        "hero_lead": "Belconnen town centre has a real mix — units, townhouses and older standalone homes around the edges of the lake, plus the newer apartments closer to the mall. Strata gardens, shared common areas, and compact courtyards that still need regular attention even if they're not big quarter-acre blocks.",
        "why_paragraph": "Belconnen town centre jobs range from quick courtyard mows at apartment complexes to full garden maintenance for strata committees. We work around tenant access, keep noise down in dense living areas, and handle the before-and-after reporting that property managers need.",
        "job_title": "Belconnen townhouse complex tidy-up",
        "job_description": "Strata-managed row of six townhouses — mowed all common areas, trimmed the boundary hedge along the footpath, edged around carparks and blew down all hard surfaces. Monthly program now in place with photo reporting to the strata manager.",
        "nearby": ["bruce", "page", "kaleen", "giralang", "macquarie"],
        "scheduling": "Usually within the week for Belconnen",
    },
    {
        "name": "Bruce",
        "slug": "bruce",
        "postcode": "2617",
        "region": "Belconnen",
        "hero_lead": "Bruce wraps around the University of Canberra and the AIS — it's a suburb of two halves. The residential streets west of Haydon Drive have solid 1970s family homes on decent blocks. East of there it's more institutional and commercial. We service the residential side thoroughly, plus rental properties near the uni that need regular upkeep.",
        "why_paragraph": "Bruce has heavier foot traffic than most Belconnen suburbs thanks to the uni, CIT and the stadium. Lawns near shared boundaries cop more wear, verges get parked on, and rental properties often go longer between maintenance visits than they should. We know the difference between a neglected lawn and a damaged one, and treat each accordingly.",
        "job_title": "Bruce rental property pre-inspection clean-up",
        "job_description": "Investment property near the uni — lawn hadn't been touched in six weeks, edges lost, weeds in the driveway cracks. Full mow, re-edge, weeded paths and front beds, blew down the driveway and patio. Landlord got before-and-after photos same day.",
        "nearby": ["belconnen", "evatt", "kaleen", "aranda", "cook"],
        "scheduling": "Usually within the week for Bruce",
    },
    {
        "name": "Charnwood",
        "slug": "charnwood",
        "postcode": "2615",
        "region": "Belconnen",
        "hero_lead": "Charnwood is classic outer Belconnen — generous blocks, wide nature strips, established trees and a lot of yards that reward regular attention. It's the kind of suburb where a fortnightly mow and edge makes a real difference to how the whole street looks, and where neighbours notice when someone's garden is tidy.",
        "why_paragraph": "Charnwood blocks are typically larger than the inner suburbs, with plenty of backyard space and long nature strips that take time to do properly. We bring the right gear for bigger runs and price it fairly — no surprises because the block turned out to be larger than expected.",
        "job_title": "Charnwood front and back full service",
        "job_description": "Large corner block with front verge, side path and a big backyard. Mowed front and back at different heights, edged all paths and the driveway, trimmed the side hedge, and cleared leaf litter from the back fence line. Fortnightly visits locked in.",
        "nearby": ["dunlop", "fraser", "florey", "macgregor"],
        "scheduling": "Usually within the week for Charnwood",
    },
    {
        "name": "Cook",
        "slug": "cook",
        "postcode": "2614",
        "region": "Belconnen",
        "hero_lead": "Cook is one of Belconnen's quieter pockets — a small suburb wedged between Aranda, Macquarie and Weetangera with a strong community feel. Established gardens, tidy streets and the kind of blocks where people take pride in their yards. The Cook shops precinct gives it a village character that most Belconnen suburbs don't have.",
        "why_paragraph": "Cook is compact and well-established, which means mature plantings, hedges that need regular shaping, and garden beds that have been evolving for decades. We respect what's already there and maintain it properly rather than just running the mower over everything.",
        "job_title": "Cook hedge and garden bed refresh",
        "job_description": "Matching pair of photinia hedges flanking the front path — reshaped to a clean taper, all faces trimmed, clippings removed. Garden beds weeded and topped up with 40mm of hardwood mulch. Paths blown clean.",
        "nearby": ["aranda", "macquarie", "weetangera", "page"],
        "scheduling": "Usually within the week for Cook",
    },
    {
        "name": "Dunlop",
        "slug": "dunlop",
        "postcode": "2615",
        "region": "Belconnen",
        "hero_lead": "Dunlop sits on Belconnen's western fringe — relatively newer homes compared to the older inner suburbs, with a mix of established blocks from the 1990s and some newer infill. Good-sized yards, plenty of couch and kikuyu lawns that grow hard in summer, and enough space that a proper mowing service makes a genuine difference.",
        "why_paragraph": "Dunlop lawns tend toward warm-season grasses that go dormant in winter and explode in summer. We adjust visit frequency and mowing height seasonally rather than running a rigid schedule that doesn't match how the grass actually grows. Saves you money in winter, keeps things tidy when it matters in the warmer months.",
        "job_title": "Dunlop seasonal lawn recovery",
        "job_description": "Kikuyu lawn that had gotten away during a hot November — scalped patches, thick runners across the garden beds. Gradually brought the height down over two visits rather than shocking it, re-edged the beds, and set up a fortnightly summer schedule.",
        "nearby": ["charnwood", "fraser", "macgregor"],
        "scheduling": "Usually within the week for Dunlop",
    },
    {
        "name": "Evatt",
        "slug": "evatt",
        "postcode": "2617",
        "region": "Belconnen",
        "hero_lead": "Evatt is a solid family suburb in central Belconnen — well-treed streets, good-sized blocks, and a lot of homes that were built in the late 1970s and still have the original garden layouts. Mature liquidambars, big hedges, and lawns that benefit from consistent care rather than the once-a-month catch-up approach.",
        "why_paragraph": "Evatt's tree canopy is one of the densest in Belconnen, which means heavy leaf drop in autumn and shaded lawns that grow differently to sun-baked yards. We adjust for that — different mowing heights in shaded areas, leaf clearing as part of the regular visit, and gutter cleaning when the liquidambars dump everything at once.",
        "job_title": "Evatt autumn leaf and gutter clean",
        "job_description": "Full autumn service — gutters cleared of liquidambar leaves, downpipes tested, all hard surfaces blown clean, then a mow and edge to finish. Before-and-after photos sent to the homeowner who was interstate.",
        "nearby": ["kaleen", "bruce", "giralang", "mckellar"],
        "scheduling": "Usually within the week for Evatt",
    },
    {
        "name": "Florey",
        "slug": "florey",
        "postcode": "2615",
        "region": "Belconnen",
        "hero_lead": "Florey has good bones — 1970s and 80s homes on decent-sized blocks, wide streets, and enough mature trees to give it real character. It's the kind of suburb where regular lawn and garden maintenance keeps everything looking sharp without needing to spend a fortune. Plenty of our fortnightly customers are in Florey and surrounding streets.",
        "why_paragraph": "Florey blocks are generous enough that a mow takes real time to do properly. We don't rush — edges are done with the line trimmer, not skipped, and we blow down all hard surfaces before we leave. The difference between a cheap mow and a proper one shows for weeks in a suburb like Florey.",
        "job_title": "Florey backyard rescue job",
        "job_description": "Backyard that had been closed off for months — ankle-deep grass, fallen branches, garden beds completely overgrown. Cut in stages, raked and removed all debris, re-established the edges and mulched the beds. Two trailer loads of green waste removed.",
        "nearby": ["higgins", "scullin", "page", "charnwood", "latham"],
        "scheduling": "Usually within the week for Florey",
    },
    {
        "name": "Fraser",
        "slug": "fraser",
        "postcode": "2615",
        "region": "Belconnen",
        "hero_lead": "Fraser is on the outer western edge of Belconnen — newer than the inner suburbs, with a mix of larger blocks and some rural-residential feel near the boundary. The kind of suburb where yards are big enough that keeping on top of them takes real commitment, and where a reliable mowing service pays for itself in time saved.",
        "why_paragraph": "Fraser properties often have larger-than-average yards and boundary areas that border open space. That means more edge work, more blowing, and sometimes dealing with grass and weeds that creep in from unmaintained reserve land. We handle all of it and leave a clean line at the boundary.",
        "job_title": "Fraser large block mow and tidy",
        "job_description": "Full mow on a 900sqm block backing onto reserve land — front, back and both side yards, all edges done, nature strip mowed, and the reserve boundary trimmed back to the fence line. Fortnightly schedule set up for summer.",
        "nearby": ["charnwood", "dunlop"],
        "scheduling": "Usually within the week for Fraser",
    },
    {
        "name": "Giralang",
        "slug": "giralang",
        "postcode": "2617",
        "region": "Belconnen",
        "hero_lead": "Giralang is compact and leafy — one of Belconnen's smaller suburbs but with well-established gardens and a strong sense of neighbourhood. The blocks are a good size without being enormous, and most have been landscaped over decades. It's the kind of suburb where consistent maintenance keeps things looking genuinely good.",
        "why_paragraph": "Giralang's compact size means we're often servicing multiple properties on the same street or neighbouring streets in a single visit. That works in your favour — efficient scheduling, no mobilisation premium, and we're already in the area so booking extra services is easy.",
        "job_title": "Giralang neighbour double-booking",
        "job_description": "Two adjacent properties booked together — full mow and edge on both, hedges trimmed along the shared boundary (from both sides), and nature strips done to a consistent height. Neighbours splitting the hedge trim cost made it very cost-effective.",
        "nearby": ["kaleen", "evatt", "mckellar"],
        "scheduling": "Usually within the week for Giralang",
    },
    {
        "name": "Hawker",
        "slug": "hawker",
        "postcode": "2614",
        "region": "Belconnen",
        "hero_lead": "Hawker has a real neighbourhood feel — quiet streets, a good local shops precinct, and blocks that have had forty-plus years to mature. The gardens here reflect long-term ownership, with established trees, defined beds, and lawns that respond well to proper seasonal care. One of the more pleasant suburbs to work in across Belconnen.",
        "why_paragraph": "Hawker is one of those suburbs where the regulars know what good maintenance looks like and appreciate it when it's done right. Mature hedges trimmed to a clean line, edges sharp, blower finish on the paths. We don't cut corners — especially in suburbs where the standard is already high.",
        "job_title": "Hawker front garden complete refresh",
        "job_description": "Mature front garden with overgrown shrubs blocking the path, hedge grown out of shape, and tired mulch in the beds. Pruned all shrubs back to size, reshaped the hedge, weeded and re-mulched the beds with 60mm of hardwood chip. The homeowner said it looked ten years younger.",
        "nearby": ["scullin", "page", "weetangera", "cook"],
        "scheduling": "Usually within the week for Hawker",
    },
    {
        "name": "Higgins",
        "slug": "higgins",
        "postcode": "2615",
        "region": "Belconnen",
        "hero_lead": "Higgins is solid outer Belconnen — family homes on generous blocks, wide verges, and a community that appreciates a tidy street. Most houses date from the late 1970s and early 1980s, which means established gardens, mature trees and lawns that have had time to settle into their character.",
        "why_paragraph": "Higgins blocks are typically big enough that the backyard alone takes a decent session to mow properly. We factor that in when quoting — you get an honest price for the full job including edges, blowing and any extras, not a lowball number that magically grows once we see the back fence.",
        "job_title": "Higgins end-of-lease garden blitz",
        "job_description": "Tenant moving out needed the garden presentable for final inspection. Full mow front and back, edges re-cut, weeds pulled from garden beds, paths blown clean. Property manager signed off without issue. Single visit, done in a day.",
        "nearby": ["florey", "holt", "scullin", "latham"],
        "scheduling": "Usually within the week for Higgins",
    },
    {
        "name": "Holt",
        "slug": "holt",
        "postcode": "2615",
        "region": "Belconnen",
        "hero_lead": "Holt wraps around the Kippax shops and has a real community centre feel. Mix of original Belconnen-era homes and some newer developments closer to the group centre. Good-sized blocks, plenty of couch grass lawns, and enough families that weekend mowing is a regular soundtrack — though our battery gear makes it a much quieter one.",
        "why_paragraph": "Holt has a lot of families with young kids and pets using the backyard hard. That means lawns that cop more wear and need a mowing approach that promotes recovery rather than just cutting short. We adjust height and frequency to keep your lawn thick and healthy, not just short.",
        "job_title": "Holt family backyard mow and safety tidy",
        "job_description": "Family property with a trampoline, swing set and a well-used backyard — mowed around all the play equipment carefully, edged the patio and paths, trimmed the side hedge and cleared fallen branches from the back fence. Set up fortnightly visits timed for when the kids are at school.",
        "nearby": ["higgins", "macgregor", "latham", "charnwood"],
        "scheduling": "Usually within the week for Holt",
    },
    {
        "name": "Kaleen",
        "slug": "kaleen",
        "postcode": "2617",
        "region": "Belconnen",
        "hero_lead": "Kaleen is one of Belconnen's bigger residential suburbs — long, quiet streets with well-maintained homes and gardens that reflect years of care. The blocks are a good size, the tree cover is solid, and there's a noticeable pride in how the streets look. We service a good number of properties in Kaleen and it shows in the regularity of the work.",
        "why_paragraph": "Kaleen is big enough that we're there most weeks servicing multiple customers on different schedules. That means we know the suburb well — which streets get the afternoon westerly that bakes the front lawn, which blocks have clay soil that holds water, and which hedges are the vigorous growers that need quarterly attention.",
        "job_title": "Kaleen quarterly hedge maintenance",
        "job_description": "Long boundary hedge along a rear fence — viburnum, about 30 metres, grown up and out over a quarter. Trimmed all three accessible faces to a clean, straight line, shaped the top, collected and removed all clippings. Before-and-after photos provided.",
        "nearby": ["belconnen", "bruce", "giralang", "evatt", "mckellar"],
        "scheduling": "Usually within the week for Kaleen",
    },
    {
        "name": "Latham",
        "slug": "latham",
        "postcode": "2615",
        "region": "Belconnen",
        "hero_lead": "Latham sits between Florey and Holt — a quiet suburb with wide streets, decent block sizes, and an established canopy that gives it a settled, comfortable feel. Most homes were built in the 1970s and 80s, and the gardens have had time to mature into something worth maintaining properly.",
        "why_paragraph": "Latham is one of those suburbs where the difference between a properly maintained garden and a neglected one is immediately obvious from the street. We keep our Latham customers' properties looking sharp with consistent visits, clean edges, and the kind of tidy finish that lifts the whole frontage.",
        "job_title": "Latham verge and frontage tidy",
        "job_description": "Wide double-verge on a corner block — mowed both nature strips, edged along the footpath and kerb on both sides, trimmed the low hedge along the front boundary, and blew down the footpath and driveway. Looks sharp from every angle now.",
        "nearby": ["florey", "holt", "higgins", "macgregor"],
        "scheduling": "Usually within the week for Latham",
    },
    {
        "name": "Macgregor",
        "slug": "macgregor",
        "postcode": "2615",
        "region": "Belconnen",
        "hero_lead": "Macgregor is a mixed suburb — the older sections have established 1980s homes on solid blocks, while the newer areas near the Ginninderra estate feel almost brand-new. That variety keeps the work interesting. Whether it's maintaining a mature garden that's been growing for decades or setting up a maintenance program for a freshly landscaped new build, we handle both.",
        "why_paragraph": "The newer homes in Macgregor often come with compact, designed gardens that need precision rather than brute force. The older sections have bigger blocks and bigger challenges. We bring the right approach for each — no one-size-fits-all mowing.",
        "job_title": "Macgregor new build garden establishment",
        "job_description": "Recently completed home with fresh turf, new garden beds and a few hedging plants just starting out. Set up a maintenance program — gentle mowing at the right height to help the turf establish, mulch top-ups, and monitoring the new plantings. Monthly visits for the first six months.",
        "nearby": ["charnwood", "holt", "latham", "dunlop"],
        "scheduling": "Usually within the week for Macgregor",
    },
    {
        "name": "Macquarie",
        "slug": "macquarie",
        "postcode": "2614",
        "region": "Belconnen",
        "hero_lead": "Macquarie is central Belconnen — well-positioned, well-treed, and well-established. The streets around the Jamison Centre have a village feel, and the residential blocks are a comfortable size with mature gardens that have been evolving since the suburb was built in the late 1960s. Some of the oldest and best-maintained gardens in the Belconnen area are right here.",
        "why_paragraph": "Macquarie's mature gardens often include species that were popular fifty years ago — established hedges, big conifers, and the kind of rose beds that need proper seasonal pruning. We treat these gardens with the respect they deserve, not the speed-run that budget operators give them.",
        "job_title": "Macquarie mature garden seasonal service",
        "job_description": "Established property with a large rose bed, two mature hedges and a well-maintained lawn. Pruned the roses for winter, shaped both hedges, mowed and edged, and top-dressed the rose bed with compost. Quarterly program now in place aligned to the seasons.",
        "nearby": ["cook", "aranda", "belconnen", "page", "hawker"],
        "scheduling": "Usually within the week for Macquarie",
    },
    {
        "name": "McKellar",
        "slug": "mckellar",
        "postcode": "2617",
        "region": "Belconnen",
        "hero_lead": "McKellar is small, quiet and leafy — one of Belconnen's more tucked-away suburbs with a strong sense of community. The blocks are a comfortable size, the gardens are established, and most homeowners here have been maintaining their properties for years. We fit right in with regular, reliable service.",
        "why_paragraph": "McKellar's position near Ginninderra Creek means some blocks get more moisture than average, which affects grass growth and weed pressure. We adjust our approach accordingly — slightly more frequent visits in the growing season and proactive weed management to stay ahead of the problem.",
        "job_paragraph": "McKellar spring kickstart",
        "job_description": "Full spring service — mowed and edged after the winter slowdown, dethatched the front lawn where it had matted, weeded all beds, and applied a slow-release organic fertiliser to kick things off for the season. Set up fortnightly visits through to April.",
        "nearby": ["evatt", "giralang", "kaleen"],
        "scheduling": "Usually within the week for McKellar",
    },
    {
        "name": "Melba",
        "slug": "melba",
        "postcode": "2615",
        "region": "Belconnen",
        "hero_lead": "Melba is right up the top of Belconnen — a quiet suburb that feels further from the city than it actually is. Good-sized blocks, wide streets, and an older demographic that values consistent, reliable service. The gardens here are well-established and most homeowners appreciate someone who turns up when they say they will.",
        "why_paragraph": "Melba properties often have larger rear gardens and boundary plantings that need regular attention. We handle the full property — not just the bits visible from the street. Front verge, side access, backyard, edges, blowing — the lot.",
        "job_title": "Melba full property maintenance start",
        "job_description": "New regular customer — initial visit to bring everything up to standard. Full mow front and back, edges re-established, overgrown shrubs trimmed back from the fence, and all paths blown clean. Now on a fortnightly cycle.",
        "nearby": ["spence", "evatt", "florey"],
        "scheduling": "Usually within the week for Melba",
    },
    {
        "name": "Page",
        "slug": "page",
        "postcode": "2614",
        "region": "Belconnen",
        "hero_lead": "Page sits right in the heart of Belconnen — close to the town centre, well-connected, and with a good mix of original 1970s homes and some newer townhouse developments. The mature street trees give Page a leafy, established feel, and most blocks have gardens that benefit from proper, regular maintenance.",
        "why_paragraph": "Page is close to everything, which means a lot of busy households that want the garden sorted without having to think about it. That's exactly what we do — turn up on schedule, do the job properly, send a text when it's done. No chasing, no missed visits.",
        "job_title": "Page townhouse courtyard and common area",
        "job_description": "Small group of townhouses — individual courtyard gardens mowed and edged, shared front lawn maintained, boundary hedge trimmed, and all common paths blown clean. Monthly visits set up with costs split between the three households.",
        "nearby": ["scullin", "hawker", "cook", "florey", "belconnen"],
        "scheduling": "Usually within the week for Page",
    },
    {
        "name": "Scullin",
        "slug": "scullin",
        "postcode": "2614",
        "region": "Belconnen",
        "hero_lead": "Scullin is a well-positioned Belconnen suburb with quick access to both the Belconnen town centre and the Calvary Hospital precinct. The homes are mostly 1970s-era on good blocks with established gardens. It's a tidy suburb overall, and our regular customers here help keep it that way.",
        "why_paragraph": "Scullin's proximity to the hospital precinct means a few of our customers here are shift workers — they sleep during the day and our quiet battery equipment is genuinely appreciated. No petrol mowers screaming outside the bedroom window at 8am.",
        "job_title": "Scullin shift-worker-friendly mow",
        "job_description": "Regular fortnightly customer who works night shifts. We schedule for early afternoon, use the battery mower and blower (about 30% the noise of petrol), and text completion photos rather than knocking. They've said the neighbours have asked who we are because they barely heard us.",
        "nearby": ["page", "hawker", "florey", "higgins"],
        "scheduling": "Usually within the week for Scullin",
    },
    {
        "name": "Spence",
        "slug": "spence",
        "postcode": "2615",
        "region": "Belconnen",
        "hero_lead": "Spence is at the northern end of Belconnen — quiet, residential, and with good-sized blocks that have had decades to establish. The gardens here tend to be practical and low-key rather than manicured, but they still need regular attention to stay on top of things, especially through the growing season.",
        "why_paragraph": "Spence borders open space and some of the properties back onto reserves, which means grass and weeds can encroach from both directions. We maintain a clean boundary and keep the property-side growth under control, so the reserve doesn't slowly take over your backyard.",
        "job_title": "Spence reserve boundary maintenance",
        "job_description": "Property backing onto nature reserve — rear boundary had become overgrown with grass and weeds growing through the fence line. Cleared and trimmed back to the fence, mowed the backyard, edged all paths and re-established a clean line between garden and reserve.",
        "nearby": ["melba", "evatt", "florey"],
        "scheduling": "Usually within the week for Spence",
    },
    {
        "name": "Weetangera",
        "slug": "weetangera",
        "postcode": "2614",
        "region": "Belconnen",
        "hero_lead": "Weetangera sits on the southern edge of Belconnen, bordering the ANU campus side of the ridge. It's a small, established suburb with a bushland backdrop, generous blocks and mature gardens that reflect careful long-term ownership. Some of the most pleasant residential streets in the Belconnen area are right here.",
        "why_paragraph": "Weetangera's proximity to the ridgeline means leaf litter, wildlife-friendly gardens, and some blocks with significant grade changes. We handle sloped sections safely, work around native plantings with care, and keep the mowing height appropriate for the conditions on each block.",
        "job_title": "Weetangera sloped front yard mow and edge",
        "job_description": "Steep front yard that rolls down to the footpath — careful mowing on the grade with the push mower (not the ride-on — too dangerous on a slope like this), crisp edges along the path and driveway, and a blower finish on all hard surfaces. Looks great from the street.",
        "nearby": ["cook", "aranda", "hawker", "macquarie"],
        "scheduling": "Usually within the week for Weetangera",
    },
]

# Fix McKellar's job_title key
for s in SUBURBS:
    if "job_paragraph" in s:
        s["job_title"] = s.pop("job_paragraph")


TEMPLATE = '''<!doctype html>
<html lang="en-AU">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Lawn mowing &amp; garden care in {name}, ACT | EcoMow Canberra</title>
<meta name="description" content="Battery-powered lawn mowing, hedging and garden care in {name} {postcode}. Quick scheduling, tidy finishes, neighbour-friendly. Call Kai on 0414 058 552.">
<link rel="canonical" href="https://ecomowcanberra.com.au/suburbs/{slug}/">

<meta property="og:type" content="website">
<meta property="og:title" content="Lawn mowing &amp; garden care in {name}, ACT | EcoMow Canberra">
<meta property="og:description" content="Battery-powered lawn mowing, hedging and garden care in {name} {postcode}. Quick scheduling, tidy finishes, neighbour-friendly. Call Kai on 0414 058 552.">
<meta property="og:url" content="https://ecomowcanberra.com.au/suburbs/{slug}/">
<meta property="og:image" content="https://ecomowcanberra.com.au/assets/images/og-image.jpg">
<meta property="og:locale" content="en_AU">
<meta name="twitter:card" content="summary_large_image">

<meta name="theme-color" content="#0B3D2A">

<link rel="preconnect" href="https://fonts.googleapis.com" crossorigin>
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap">
<link rel="stylesheet" href="/assets/css/styles.css">

<link rel="icon" href="/favicon.ico" sizes="any">
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="/apple-touch-icon.png">

<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "LocalBusiness",
  "@id": "https://ecomowcanberra.com.au/#business",
  "name": "EcoMow Canberra",
  "image": "https://ecomowcanberra.com.au/assets/images/logo.png",
  "url": "https://ecomowcanberra.com.au/suburbs/{slug}/",
  "telephone": "+61414058552",
  "email": "ecomowcanberra@gmail.com",
  "priceRange": "$$",
  "address": {{
    "@type": "PostalAddress",
    "addressLocality": "Hackett",
    "addressRegion": "ACT",
    "postalCode": "2602",
    "addressCountry": "AU"
  }},
  "areaServed": {{
    "@type": "Place",
    "name": "{name}, ACT"
  }},
  "openingHoursSpecification": [
    {{
      "@type": "OpeningHoursSpecification",
      "dayOfWeek": ["Monday","Tuesday","Wednesday","Thursday","Friday"],
      "opens": "07:00",
      "closes": "19:00"
    }},
    {{
      "@type": "OpeningHoursSpecification",
      "dayOfWeek": ["Saturday","Sunday"],
      "opens": "10:00",
      "closes": "16:00"
    }}
  ],
  "aggregateRating": {{
    "@type": "AggregateRating",
    "ratingValue": "4.9",
    "reviewCount": "29",
    "bestRating": "5",
    "worstRating": "1"
  }}
}}
</script>
<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {{
      "@type": "Question",
      "name": "How soon can you book {name} jobs?",
      "acceptedAnswer": {{
        "@type": "Answer",
        "text": "{scheduling} — we're Hackett-based and cover all of Belconnen. Text your address and preferred times and we'll confirm the next available window."
      }}
    }},
    {{
      "@type": "Question",
      "name": "Do you work early mornings in {name}?",
      "acceptedAnswer": {{
        "@type": "Answer",
        "text": "Yes, within 07:00 to 19:00 on weekdays and 10:00 to 16:00 on weekends. Our battery gear keeps noise low for neighbours, and if you've got shift workers nearby we'll schedule accordingly."
      }}
    }},
    {{
      "@type": "Question",
      "name": "Do you remove green waste from {name} properties?",
      "acceptedAnswer": {{
        "@type": "Answer",
        "text": "Yes. We use your green bin where possible and can remove excess on request. For larger cleanups we bring the trailer."
      }}
    }},
    {{
      "@type": "Question",
      "name": "Can you maintain verges and nature strips in {name}?",
      "acceptedAnswer": {{
        "@type": "Answer",
        "text": "Yes, we mow and edge verges and keep paths clean. If your street has specific rules or access notes, let us know."
      }}
    }},
    {{
      "@type": "Question",
      "name": "Do I need to be home?",
      "acceptedAnswer": {{
        "@type": "Answer",
        "text": "No. Provide access instructions and we'll handle the rest. We can send photo updates when finished."
      }}
    }},
    {{
      "@type": "Question",
      "name": "Can I set a regular plan for {name}?",
      "acceptedAnswer": {{
        "@type": "Answer",
        "text": "Yes. Weekly, fortnightly or monthly depending on growth. You can adjust by SMS anytime — no lock-in contracts."
      }}
    }}
  ]
}}
</script>
<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "BreadcrumbList",
  "itemListElement": [
    {{ "@type": "ListItem", "position": 1, "name": "Home", "item": "https://ecomowcanberra.com.au/" }},
    {{ "@type": "ListItem", "position": 2, "name": "Suburbs", "item": "https://ecomowcanberra.com.au/suburbs/" }},
    {{ "@type": "ListItem", "position": 3, "name": "{name}", "item": "https://ecomowcanberra.com.au/suburbs/{slug}/" }}
  ]
}}
</script>
</head>
<body>

<a class="skip-link" href="#main">Skip to main content</a>

<header class="site-header" role="banner">
  <div class="site-header__inner">
    <a class="brand" href="/" aria-label="EcoMow Canberra — home">
      <img class="brand__logo" src="/assets/images/logo.png" alt="EcoMow Canberra — eco-friendly lawn care" width="220" height="56">
    </a>

    <nav class="nav" aria-label="Primary">
      <ul class="nav__list">
        <li><a class="nav__link" href="/">Home</a></li>
        <li><a class="nav__link" href="/services/">Services</a></li>
        <li><a class="nav__link" href="/suburbs/" aria-current="page">Suburbs</a></li>
        <li><a class="nav__link" href="/reviews/">Reviews</a></li>
        <li><a class="nav__link" href="/gallery/">Gallery</a></li>
        <li><a class="nav__link" href="/customer-charter/">Charter</a></li>
        <li><a class="nav__link" href="/contact/">Contact</a></li>
      </ul>
    </nav>

    <a class="btn btn--primary header-cta" href="tel:+61414058552">
      <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" width="18" height="18" aria-hidden="true"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6A19.79 19.79 0 0 1 2.12 4.18 2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72c.13.96.37 1.9.72 2.81a2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45c.91.35 1.85.59 2.81.72A2 2 0 0 1 22 16.92z"/></svg>
      Call 0414 058 552
    </a>

    <button class="menu-toggle" type="button" aria-expanded="false" aria-controls="mobile-nav" aria-label="Open menu">
      <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" width="24" height="24" aria-hidden="true"><line x1="4" y1="7" x2="20" y2="7"/><line x1="4" y1="12" x2="20" y2="12"/><line x1="4" y1="17" x2="20" y2="17"/></svg>
    </button>
  </div>

  <div class="mobile-nav" id="mobile-nav" aria-hidden="true">
    <ul class="mobile-nav__list">
      <li><a class="mobile-nav__link" href="/">Home</a></li>
      <li><a class="mobile-nav__link" href="/services/">Services</a></li>
      <li><a class="mobile-nav__link" href="/suburbs/" aria-current="page">Suburbs we service</a></li>
      <li><a class="mobile-nav__link" href="/reviews/">Reviews</a></li>
      <li><a class="mobile-nav__link" href="/gallery/">Gallery</a></li>
      <li><a class="mobile-nav__link" href="/customer-charter/">Customer charter</a></li>
      <li><a class="mobile-nav__link" href="/contact/">Contact &amp; quote</a></li>
    </ul>
    <a class="btn btn--primary btn--block" href="tel:+61414058552">Call Kai — 0414 058 552</a>
  </div>
</header>
<main id="main">

<nav class="container" aria-label="Breadcrumb" style="padding-top:var(--s-4);padding-bottom:0">
  <ol style="display:flex;flex-wrap:wrap;gap:var(--s-2);list-style:none;padding:0;margin:0;font-size:var(--fs-xs);color:var(--ink-500)">
    <li><a href="/" style="color:var(--ink-500)">Home</a></li>
    <li aria-hidden="true">›</li>
    <li><a href="/suburbs/" style="color:var(--ink-500)">Suburbs</a></li>
    <li aria-hidden="true">›</li>
    <li aria-current="page" style="color:var(--ink-700);font-weight:600">{name}</li>
  </ol>
</nav>

<section class="hero" aria-labelledby="hero-heading" style="padding:var(--s-7) 0 var(--s-8)">
  <div class="container">
    <div class="hero__inner">
      <div class="hero__grid">
        <div>
          <span class="eyebrow" style="color:#F2C94C">{region} · {postcode}</span>
          <h1 id="hero-heading">Lawn mowing and garden care in {name}, ACT.</h1>
          <p class="lead">{hero_lead}</p>

          <div class="hero__badges">
            <span class="badge"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M12 2l2.39 6.95H21l-5.3 3.85L17.78 20 12 16.1 6.22 20l2.08-7.2L3 8.95h6.61L12 2z"/></svg> 4.9 ★ Google</span>
            <span class="badge"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"/><circle cx="12" cy="10" r="3"/></svg> {region}</span>
            <span class="badge"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="5" y="7" width="14" height="10" rx="2"/><line x1="19" y1="11" x2="21" y2="11"/></svg> Battery only</span>
            <span class="badge"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="12" cy="12" r="10"/><path d="M12 6v6l4 2"/></svg> Since 2022</span>
          </div>

          <div class="btn-row">
            <a class="btn btn--gold btn--lg" href="/contact/#quote-form">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" width="20" height="20" aria-hidden="true"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><polyline points="14 2 14 8 20 8"/><line x1="9" y1="13" x2="15" y2="13"/><line x1="9" y1="17" x2="15" y2="17"/></svg>
              Get a quote online
            </a>
            <a class="btn btn--ghost btn--lg" href="tel:+61414058552">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" width="20" height="20" aria-hidden="true"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6A19.79 19.79 0 0 1 2.12 4.18 2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72c.13.96.37 1.9.72 2.81a2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45c.91.35 1.85.59 2.81.72A2 2 0 0 1 22 16.92z"/></svg>
              Call Kai
            </a>
            <a class="btn btn--ghost btn--lg" href="sms:+61414058552">Text for a quote</a>
          </div>
        </div>
      </div>
    </div>
  </div>
</section>

<section class="section section--cream" aria-labelledby="services-heading">
  <div class="container">
    <div class="text-center" style="max-width:720px;margin:0 auto var(--s-7)">
      <span class="eyebrow">Services in {name}</span>
      <h2 id="services-heading">One team handles the lot, so you don't juggle multiple vendors.</h2>
      <p class="lead" style="margin-left:auto;margin-right:auto">From routine lawns and verges to full cleanups, hedging and mulching — we cover it all in {name} with quiet battery equipment and a proper tidy finish.</p>
    </div>

    <ul class="services-grid" style="list-style:none;padding:0;margin:0">
      <li>
        <div class="service-card">
          <span class="service-card__icon" aria-hidden="true"><svg viewBox="0 0 32 32" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M4 24h24"/><path d="M6 24V14l4-4h6l4 4v10"/><circle cx="10" cy="26" r="2"/><circle cx="22" cy="26" r="2"/></svg></span>
          <h3>Lawn mowing and edging</h3>
          <p>Season-right height, sharp edges, clean blower finish. Verges and nature strips included on request.</p>
          <a class="service-card__more" href="/services/lawn-mowing/">See details <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><polyline points="9 18 15 12 9 6"/></svg></a>
        </div>
      </li>
      <li>
        <div class="service-card">
          <span class="service-card__icon" aria-hidden="true"><svg viewBox="0 0 32 32" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M4 22h24"/><path d="M6 22V12c0-3 2-6 5-6h10c3 0 5 3 5 6v10"/></svg></span>
          <h3>Hedging and pruning</h3>
          <p>Accurate shaping, height control, tidy drop zones. Neat lines, clippings handled.</p>
          <a class="service-card__more" href="/services/hedge-trimming/">See details <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><polyline points="9 18 15 12 9 6"/></svg></a>
        </div>
      </li>
      <li>
        <div class="service-card">
          <span class="service-card__icon" aria-hidden="true"><svg viewBox="0 0 32 32" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M8 26L20 14"/><path d="M20 14l3-3 3 3-3 3z"/></svg></span>
          <h3>Garden work and cleanups</h3>
          <p>Weeding, leaf and debris removal, bed resets and mulch top-ups. Big one-off jobs welcome.</p>
          <a class="service-card__more" href="/services/garden-cleanups/">See details <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><polyline points="9 18 15 12 9 6"/></svg></a>
        </div>
      </li>
      <li>
        <div class="service-card">
          <span class="service-card__icon" aria-hidden="true"><svg viewBox="0 0 32 32" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="4" y="6" width="24" height="20" rx="2"/><path d="M8 14h16"/></svg></span>
          <h3>Lawn maintenance plans</h3>
          <p>Weekly, fortnightly or monthly visits matched to growth. Consistent colour and coverage all season.</p>
          <a class="service-card__more" href="/services/garden-maintenance/">See details <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><polyline points="9 18 15 12 9 6"/></svg></a>
        </div>
      </li>
      <li>
        <div class="service-card">
          <span class="service-card__icon" aria-hidden="true"><svg viewBox="0 0 32 32" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M4 12l12-8 12 8"/><path d="M6 12v14h20V12"/></svg></span>
          <h3>Gutter cleaning</h3>
          <p>Gutters cleared and accessible downpipes tested. Safety-first with before-and-after photos.</p>
          <a class="service-card__more" href="/services/gutter-cleaning/">See details <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><polyline points="9 18 15 12 9 6"/></svg></a>
        </div>
      </li>
      <li>
        <div class="service-card">
          <span class="service-card__icon" aria-hidden="true"><svg viewBox="0 0 32 32" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M16 4v24"/><path d="M10 10c-2 2-2 5 0 7"/><path d="M22 10c2 2 2 5 0 7"/><path d="M13 14c-1 1-1 3 0 4"/></svg></span>
          <h3>Tree pruning and trimming</h3>
          <p>Small to medium trees shaped, deadwood removed, safer walkways. Not in powerline hazard zones.</p>
          <a class="service-card__more" href="/services/light-tree-work/">See details <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><polyline points="9 18 15 12 9 6"/></svg></a>
        </div>
      </li>
    </ul>
  </div>
</section>

<section class="section section--paper" aria-labelledby="why-heading">
  <div class="container">
    <span class="eyebrow">Why {name} residents choose EcoMow</span>
    <h2 id="why-heading">Local, quiet, tidy — and we actually turn up.</h2>
    <p>{why_paragraph}</p>
    <ul class="commitments" style="display:grid;gap:var(--s-3);list-style:none;padding:0;margin:var(--s-5) 0 0">
      <li class="commitment" style="background:var(--green-50);border-color:var(--green-100)">
        <span class="commitment__icon" aria-hidden="true" style="background:var(--green-800);color:var(--gold-400)"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"><polyline points="20 6 9 17 4 12"/></svg></span>
        <div><h3 style="color:var(--ink-900)">Fast scheduling — we cover all of Belconnen</h3><p style="color:var(--ink-600)">Often same-week availability for {name}.</p></div>
      </li>
      <li class="commitment" style="background:var(--green-50);border-color:var(--green-100)">
        <span class="commitment__icon" aria-hidden="true" style="background:var(--green-800);color:var(--gold-400)"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"><polyline points="20 6 9 17 4 12"/></svg></span>
        <div><h3 style="color:var(--ink-900)">Quiet battery gear, no petrol smell</h3><p style="color:var(--ink-600)">Kind to kids, pets and shift-worker neighbours.</p></div>
      </li>
      <li class="commitment" style="background:var(--green-50);border-color:var(--green-100)">
        <span class="commitment__icon" aria-hidden="true" style="background:var(--green-800);color:var(--gold-400)"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"><polyline points="20 6 9 17 4 12"/></svg></span>
        <div><h3 style="color:var(--ink-900)">Tidy finishes with green waste handled</h3><p style="color:var(--ink-600)">Your green bin, mulched on site, or taken away.</p></div>
      </li>
      <li class="commitment" style="background:var(--green-50);border-color:var(--green-100)">
        <span class="commitment__icon" aria-hidden="true" style="background:var(--green-800);color:var(--gold-400)"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"><polyline points="20 6 9 17 4 12"/></svg></span>
        <div><h3 style="color:var(--ink-900)">SMS-based comms and photo updates</h3><p style="color:var(--ink-600)">No phone tag. Photos sent on request.</p></div>
      </li>
    </ul>
  </div>
</section>

<section class="section section--cream" aria-labelledby="job-heading">
  <div class="container-narrow">
    <div class="job-card">
      <span class="eyebrow">Recent job near you</span>
      <h3 id="job-heading">{job_title}</h3>
      <p>{job_description}</p>
      <a class="btn btn--outline" href="/gallery/">See more of our work</a>
    </div>
  </div>
</section>

<section class="section section--paper" aria-labelledby="local-review">
  <div class="container-narrow">
    <div class="text-center" style="max-width:620px;margin:0 auto var(--s-6)">
      <span class="eyebrow">From a Canberra customer</span>
      <h2 id="local-review">What our customers say.</h2>
    </div>
    <div class="review-card" style="max-width:560px;margin:0 auto">
      <span class="stars" aria-label="5 out of 5 stars"><svg viewBox="0 0 24 24" fill="currentColor" width="18" height="18" aria-hidden="true"><path d="M12 2l2.39 6.95H21l-5.3 3.85L17.78 20 12 16.1 6.22 20l2.08-7.2L3 8.95h6.61L12 2z"/></svg><svg viewBox="0 0 24 24" fill="currentColor" width="18" height="18" aria-hidden="true"><path d="M12 2l2.39 6.95H21l-5.3 3.85L17.78 20 12 16.1 6.22 20l2.08-7.2L3 8.95h6.61L12 2z"/></svg><svg viewBox="0 0 24 24" fill="currentColor" width="18" height="18" aria-hidden="true"><path d="M12 2l2.39 6.95H21l-5.3 3.85L17.78 20 12 16.1 6.22 20l2.08-7.2L3 8.95h6.61L12 2z"/></svg><svg viewBox="0 0 24 24" fill="currentColor" width="18" height="18" aria-hidden="true"><path d="M12 2l2.39 6.95H21l-5.3 3.85L17.78 20 12 16.1 6.22 20l2.08-7.2L3 8.95h6.61L12 2z"/></svg><svg viewBox="0 0 24 24" fill="currentColor" width="18" height="18" aria-hidden="true"><path d="M12 2l2.39 6.95H21l-5.3 3.85L17.78 20 12 16.1 6.22 20l2.08-7.2L3 8.95h6.61L12 2z"/></svg></span>
      <blockquote class="review-card__quote">{review_quote}</blockquote>
      <div class="review-card__meta">
        <div>
          <div class="review-card__name">{review_name}</div>
          <div class="review-card__suburb">{review_suburb}</div>
        </div>
        <a href="/reviews/" style="font-size:var(--fs-xs)">All reviews →</a>
      </div>
    </div>
  </div>
</section>

<section class="section section--cream" aria-labelledby="nearby-heading">
  <div class="container-narrow">
    <span class="eyebrow">Nearby Belconnen suburbs</span>
    <h2 id="nearby-heading">We also service these suburbs next to {name}.</h2>
    <p>Same quiet, battery-powered service, same tidy finish. If you're on a street that borders {name}, chances are we're there most weeks.</p>
    <nav class="nearby" aria-label="Nearby suburbs we service">
{nearby_links}
    </nav>
  </div>
</section>

<section class="section section--paper" aria-labelledby="faq-heading">
  <div class="container-narrow">
    <div class="text-center" style="max-width:620px;margin:0 auto var(--s-7)">
      <span class="eyebrow">Questions from {name}</span>
      <h2 id="faq-heading">{name} FAQs.</h2>
    </div>

    <div class="faqs">
      <details class="faq"><summary>How soon can you book {name} jobs?</summary><div class="faq__body"><p>{scheduling} — we're Hackett-based and cover all of Belconnen. Text your address and preferred times and we'll confirm the next available window.</p></div></details>
      <details class="faq"><summary>Do you work early mornings in {name}?</summary><div class="faq__body"><p>Yes, within 07:00–19:00 on weekdays and 10:00–16:00 on weekends. Our battery gear keeps noise low for neighbours, and if you've got shift-workers or babies nearby we'll schedule accordingly.</p></div></details>
      <details class="faq"><summary>Do you remove green waste from {name}?</summary><div class="faq__body"><p>Yes. We use your green bin where possible, and can remove excess on request. For big cleanups we bring the trailer.</p></div></details>
      <details class="faq"><summary>Can you maintain verges and nature strips in {name}?</summary><div class="faq__body"><p>Yes, we mow and edge verges and keep paths clean. If your street has specific rules, let us know and we'll work with them.</p></div></details>
      <details class="faq"><summary>Do I need to be home?</summary><div class="faq__body"><p>No. Provide access instructions and we'll handle the rest. We can send photos when finished so you know it's done.</p></div></details>
      <details class="faq"><summary>Can I set a regular plan for {name}?</summary><div class="faq__body"><p>Yes. Weekly, fortnightly or monthly depending on growth. You can adjust by SMS anytime — no lock-in contracts.</p></div></details>
    </div>
  </div>
</section>

<section class="section" aria-labelledby="final-heading">
  <div class="container-narrow">
    <div class="final-cta">
      <h2 id="final-heading">Ready for a tidy lawn and garden in {name}?</h2>
      <p>Call Kai on 0414 058 552, text for a fast quote with your address and photos, or use our contact form and we'll reply quickly.</p>
      <div class="btn-row">
        <a class="btn btn--gold btn--lg" href="/contact/#quote-form">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" width="20" height="20" aria-hidden="true"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><polyline points="14 2 14 8 20 8"/><line x1="9" y1="13" x2="15" y2="13"/><line x1="9" y1="17" x2="15" y2="17"/></svg>
          Get a quote online
        </a>
        <a class="btn btn--ghost btn--lg" href="tel:+61414058552">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" width="20" height="20" aria-hidden="true"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6A19.79 19.79 0 0 1 2.12 4.18 2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72c.13.96.37 1.9.72 2.81a2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45c.91.35 1.85.59 2.81.72A2 2 0 0 1 22 16.92z"/></svg>
          Call Kai — 0414 058 552
        </a>
        <a class="btn btn--ghost btn--lg" href="sms:+61414058552">Text for a fast quote</a>
      </div>
    </div>
  </div>
</section>

</main>

<footer class="site-footer" role="contentinfo">
  <div class="container">
    <div class="footer-grid">
      <div class="footer__brand">
        <a class="brand" href="/" aria-label="EcoMow Canberra — home">
          <img class="brand__logo" src="/assets/images/logo.png" alt="EcoMow Canberra — eco-friendly lawn care" width="220" height="56">
        </a>
        <p>Quiet, clean lawn care across Canberra. Battery powered. Solar charged. Based in Hackett.</p>
      </div>

      <div class="footer">
        <h3>Contact</h3>
        <ul>
          <li><a href="tel:+61414058552">0414 058 552</a></li>
          <li><a href="mailto:ecomowcanberra@gmail.com">ecomowcanberra@gmail.com</a></li>
          <li>Hackett ACT 2602</li>
          <li><a href="https://www.instagram.com/ecomow_canberra/" rel="noopener">@ecomow_canberra</a></li>
        </ul>
      </div>

      <div class="footer">
        <h3>Hours</h3>
        <ul>
          <li>Mon–Fri: 7am–7pm</li>
          <li>Sat–Sun: 10am–4pm</li>
        </ul>
      </div>

      <div class="footer">
        <h3>Quick links</h3>
        <ul>
          <li><a href="/services/">Services</a></li>
          <li><a href="/suburbs/">Suburbs</a></li>
          <li><a href="/reviews/">Reviews</a></li>
          <li><a href="/gallery/">Gallery</a></li>
          <li><a href="/customer-charter/">Customer charter</a></li>
          <li><a href="/contact/">Contact</a></li>
        </ul>
      </div>
    </div>

    <div class="footer-bottom">
      <div>&copy; 2026 EcoMow Canberra. Established 2022. All rights reserved.</div>
      <div>Quiet. Clean. Canberra wide.</div>
    </div>
  </div>
</footer>

<nav class="mobile-bar" aria-label="Quick contact">
  <a href="tel:+61414058552" class="mobile-bar__primary">
    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6A19.79 19.79 0 0 1 2.12 4.18 2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72c.13.96.37 1.9.72 2.81a2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45c.91.35 1.85.59 2.81.72A2 2 0 0 1 22 16.92z"/></svg>
    Call Kai
  </a>
  <a href="sms:+61414058552">
    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"/></svg>
    Text
  </a>
  <a href="/contact/#quote-form">
    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><polyline points="14 2 14 8 20 8"/><line x1="9" y1="13" x2="15" y2="13"/><line x1="9" y1="17" x2="15" y2="17"/></svg>
    Quote
  </a>
</nav>

<script src="/assets/js/nav.js" defer></script>
</body>
</html>'''


# All known suburb slugs (existing + new Belconnen)
ALL_SUBURB_SLUGS = {s["slug"] for s in SUBURBS}
# Plus existing suburbs
EXISTING = {"ainslie","barton","braddon","campbell","chifley","curtin","deakin",
            "dickson","downer","farrer","forrest","garran","griffith","hackett",
            "hughes","isaacs","kingston","lyneham","lyons","mawson","narrabundah",
            "oconnor","omalley","pearce","phillip","red-hill","reid","torrens",
            "turner","watson","yarralumla"}
ALL_SUBURB_SLUGS.update(EXISTING)


def suburb_display_name(slug):
    """Convert slug to display name."""
    names = {s["slug"]: s["name"] for s in SUBURBS}
    # Add existing suburbs
    names.update({
        "ainslie": "Ainslie", "barton": "Barton", "braddon": "Braddon",
        "campbell": "Campbell", "chifley": "Chifley", "curtin": "Curtin",
        "deakin": "Deakin", "dickson": "Dickson", "downer": "Downer",
        "farrer": "Farrer", "forrest": "Forrest", "garran": "Garran",
        "griffith": "Griffith", "hackett": "Hackett", "hughes": "Hughes",
        "isaacs": "Isaacs", "kingston": "Kingston", "lyneham": "Lyneham",
        "lyons": "Lyons", "mawson": "Mawson", "narrabundah": "Narrabundah",
        "oconnor": "O'Connor", "omalley": "O'Malley", "pearce": "Pearce",
        "phillip": "Phillip", "red-hill": "Red Hill", "reid": "Reid",
        "torrens": "Torrens", "turner": "Turner", "watson": "Watson",
        "yarralumla": "Yarralumla",
    })
    return names.get(slug, slug.replace("-", " ").title())


def generate():
    base = os.path.dirname(os.path.abspath(__file__))
    suburbs_dir = os.path.join(base, "suburbs")

    for i, suburb in enumerate(SUBURBS):
        review = REVIEWS[i % len(REVIEWS)]

        # Build nearby links
        nearby_links = []
        for ns in suburb["nearby"]:
            display = suburb_display_name(ns)
            nearby_links.append(f'      <a href="/suburbs/{ns}/">{display}</a>')

        html = TEMPLATE.format(
            name=suburb["name"],
            slug=suburb["slug"],
            postcode=suburb["postcode"],
            region=suburb["region"],
            hero_lead=suburb["hero_lead"],
            why_paragraph=suburb["why_paragraph"],
            job_title=suburb["job_title"],
            job_description=suburb["job_description"],
            scheduling=suburb["scheduling"],
            review_quote=review[0],
            review_name=review[1],
            review_suburb=review[2],
            nearby_links="\n".join(nearby_links),
        )

        # Create directory and write file
        suburb_dir = os.path.join(suburbs_dir, suburb["slug"])
        os.makedirs(suburb_dir, exist_ok=True)
        filepath = os.path.join(suburb_dir, "index.html")
        with open(filepath, "w") as f:
            f.write(html)
        print(f"  Created: suburbs/{suburb['slug']}/index.html")

    print(f"\nGenerated {len(SUBURBS)} suburb pages.")


if __name__ == "__main__":
    generate()
