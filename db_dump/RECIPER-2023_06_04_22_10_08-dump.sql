--
-- PostgreSQL database dump
--

-- Dumped from database version 15.2
-- Dumped by pg_dump version 15.2

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: added_recipes; Type: TABLE; Schema: public; Owner: atip
--

CREATE TABLE public.added_recipes (
    user_id integer NOT NULL,
    recipe_id integer NOT NULL,
    add_timestamp timestamp without time zone
);


ALTER TABLE public.added_recipes OWNER TO atip;

--
-- Name: categories; Type: TABLE; Schema: public; Owner: atip
--

CREATE TABLE public.categories (
    name text,
    category_id integer NOT NULL
);


ALTER TABLE public.categories OWNER TO atip;

--
-- Name: classify; Type: TABLE; Schema: public; Owner: atip
--

CREATE TABLE public.classify (
    recipe_id integer NOT NULL,
    category_id integer NOT NULL,
    category_type text
);


ALTER TABLE public.classify OWNER TO atip;

--
-- Name: courses; Type: VIEW; Schema: public; Owner: atip
--

CREATE VIEW public.courses AS
 SELECT classify.recipe_id,
    classify.category_id,
    classify.category_type
   FROM public.classify
  WHERE (classify.category_type = 'course'::text);


ALTER TABLE public.courses OWNER TO atip;

--
-- Name: cuisines; Type: VIEW; Schema: public; Owner: atip
--

CREATE VIEW public.cuisines AS
 SELECT classify.recipe_id,
    classify.category_id,
    classify.category_type
   FROM public.classify
  WHERE (classify.category_type = 'cuisine'::text);


ALTER TABLE public.cuisines OWNER TO atip;

--
-- Name: favorite_recipes; Type: TABLE; Schema: public; Owner: atip
--

CREATE TABLE public.favorite_recipes (
    user_id integer NOT NULL,
    recipe_id integer NOT NULL
);


ALTER TABLE public.favorite_recipes OWNER TO atip;

--
-- Name: ingredients; Type: TABLE; Schema: public; Owner: atip
--

CREATE TABLE public.ingredients (
    id integer NOT NULL,
    recipe_id integer,
    name text,
    amount double precision,
    unit text
);


ALTER TABLE public.ingredients OWNER TO atip;

--
-- Name: instructions; Type: TABLE; Schema: public; Owner: atip
--

CREATE TABLE public.instructions (
    id integer NOT NULL,
    recipe_id integer,
    step integer,
    detail text
);


ALTER TABLE public.instructions OWNER TO atip;

--
-- Name: meals; Type: VIEW; Schema: public; Owner: atip
--

CREATE VIEW public.meals AS
 SELECT classify.recipe_id,
    classify.category_id,
    classify.category_type
   FROM public.classify
  WHERE (classify.category_type = 'meal'::text);


ALTER TABLE public.meals OWNER TO atip;

--
-- Name: new_recipes; Type: TABLE; Schema: public; Owner: atip
--

CREATE TABLE public.new_recipes (
    id integer NOT NULL,
    name text,
    duration_minute integer,
    health_score integer,
    serving integer,
    image integer,
    user_id integer
);


ALTER TABLE public.new_recipes OWNER TO atip;

--
-- Name: others; Type: VIEW; Schema: public; Owner: atip
--

CREATE VIEW public.others AS
 SELECT classify.recipe_id,
    classify.category_id,
    classify.category_type
   FROM public.classify
  WHERE (classify.category_type = 'other'::text);


ALTER TABLE public.others OWNER TO atip;

--
-- Name: recipes; Type: TABLE; Schema: public; Owner: atip
--

CREATE TABLE public.recipes (
    id bigint NOT NULL,
    name text,
    duration_minute integer,
    image text,
    calories integer,
    serving integer
);


ALTER TABLE public.recipes OWNER TO atip;

--
-- Name: user_info; Type: TABLE; Schema: public; Owner: atip
--

CREATE TABLE public.user_info (
    id integer NOT NULL,
    username text,
    password text,
    logged_in boolean,
    first_name text,
    last_name text
);


ALTER TABLE public.user_info OWNER TO atip;

--
-- Name: user_log; Type: TABLE; Schema: public; Owner: atip
--

CREATE TABLE public.user_log (
    user_id integer,
    logged_in_at timestamp without time zone NOT NULL
);


ALTER TABLE public.user_log OWNER TO atip;

--
-- Data for Name: added_recipes; Type: TABLE DATA; Schema: public; Owner: atip
--

COPY public.added_recipes (user_id, recipe_id, add_timestamp) FROM stdin;
1	716344	2023-05-28 05:07:05
1	716345	2023-05-28 10:33:41
1	716346	2023-05-30 15:11:47
\.


--
-- Data for Name: categories; Type: TABLE DATA; Schema: public; Owner: atip
--

COPY public.categories (name, category_id) FROM stdin;
breakfast	4
antipasti	1
appetizer	3
antipasto	2
brunch	5
condiment	6
dinner	7
dip	8
fingerfood	9
hor d'oeuvre	10
lunch	11
main course	12
main dish	13
marinade	14
morning meal	15
salad	16
sauce	17
seasoning	18
side dish	19
snack	20
spread	21
starter	22
side dish	23
beverage	24
drink	25
dessert	26
meat	27
seafood	28
vegetable	29
other	30
\.


--
-- Data for Name: classify; Type: TABLE DATA; Schema: public; Owner: atip
--

COPY public.classify (recipe_id, category_id, category_type) FROM stdin;
633338	23	course
29	20	cuisine
647524	11	meal
30	20	cuisine
647524	12	course
647524	13	course
39	20	cuisine
647524	7	meal
643829	1	cuisine
643829	22	course
43	20	cuisine
643829	20	cuisine
643829	3	course
643829	2	cuisine
643829	10	cuisine
716300	11	meal
716300	12	course
716300	13	course
716300	7	meal
658136	11	meal
658136	12	course
658136	13	course
658136	7	meal
715574	24	beverage
715574	25	beverage
649230	11	meal
649230	12	course
649230	13	course
649230	7	meal
644357	11	meal
644357	12	course
644357	13	course
644357	7	meal
654886	19	course
654886	11	meal
654886	12	course
654886	13	course
654886	7	meal
632797	19	course
654435	11	meal
654435	12	course
654435	13	course
654435	7	meal
19	12	course
42	13	course
631814	27	ingredient
632797	27	ingredient
633324	27	ingredient
633338	27	ingredient
634698	27	ingredient
716342	27	ingredient
641559	27	ingredient
645694	27	ingredient
645710	27	ingredient
42	27	ingredient
645824	27	ingredient
19	13	course
645879	27	ingredient
50	27	ingredient
647524	27	ingredient
649024	27	ingredient
649034	27	ingredient
649230	27	ingredient
649722	27	ingredient
46	27	ingredient
30	16	cuisine
88	27	ingredient
39	16	cuisine
57	27	ingredient
658136	27	ingredient
660133	27	ingredient
659285	27	ingredient
661570	27	ingredient
662744	27	ingredient
642125	27	ingredient
54	28	ingredient
92	28	ingredient
25	28	ingredient
644357	28	ingredient
60	28	ingredient
654435	28	ingredient
43	28	ingredient
39	28	ingredient
37	28	ingredient
12	28	ingredient
48	28	ingredient
96	28	ingredient
64	28	ingredient
86	28	ingredient
75	28	ingredient
664975	28	ingredient
663175	28	ingredient
25	19	course
79	29	ingredient
39	19	course
16	29	ingredient
634404	29	ingredient
12	19	course
37	19	course
30	19	course
634854	29	ingredient
89	29	ingredient
636857	29	ingredient
29	29	ingredient
76	29	ingredient
66	29	ingredient
62	29	ingredient
97	29	ingredient
19	29	ingredient
715631	29	ingredient
71	29	ingredient
643829	29	ingredient
67	29	ingredient
30	29	ingredient
60	29	ingredient
50	29	ingredient
646825	29	ingredient
652061	29	ingredient
654485	29	ingredient
654886	29	ingredient
655130	29	ingredient
655806	29	ingredient
716300	29	ingredient
29	22	course
30	22	course
80	29	ingredient
37	29	ingredient
39	22	course
96	29	ingredient
43	22	course
642125	29	ingredient
715574	29	ingredient
664643	29	ingredient
665574	29	ingredient
50	20	cuisine
716344	4	meal
716346	4	meal
53	20	cuisine
54	20	cuisine
62	20	cuisine
66	20	cuisine
67	20	cuisine
633338	19	course
649722	1	cuisine
649722	22	course
649722	20	cuisine
649722	3	course
649722	2	cuisine
649722	10	cuisine
645879	11	meal
645879	12	course
645879	13	course
645879	7	meal
649024	11	meal
649024	12	course
649024	13	course
649024	7	meal
645710	11	meal
645710	12	course
645710	13	course
645710	7	meal
632629	26	dessert
663175	1	cuisine
663175	22	course
663175	20	cuisine
663175	3	course
663175	2	cuisine
663175	10	cuisine
661570	11	meal
661570	12	course
661570	13	course
661570	7	meal
655806	19	course
655806	11	meal
655806	12	course
655806	13	course
655806	7	meal
641559	11	meal
641559	12	course
641559	13	course
641559	7	meal
655130	1	cuisine
655130	22	course
655130	20	cuisine
655130	3	course
655130	2	cuisine
655130	10	cuisine
66	2	cuisine
46	7	meal
64	11	meal
68	11	meal
75	13	course
68	13	course
57	13	course
53	16	cuisine
62	16	cuisine
60	19	course
75	19	course
76	19	course
62	19	course
68	19	course
80	19	course
71	19	course
79	19	course
53	19	course
46	19	course
48	19	course
50	22	course
53	22	course
54	22	course
62	22	course
66	22	course
67	22	course
66	9	cuisine
716345	4	meal
54	10	cuisine
29	10	cuisine
53	10	cuisine
716342	11	meal
716342	12	course
54	1	cuisine
716342	13	course
716342	7	meal
67	1	cuisine
654485	15	meal
654485	5	meal
654485	4	meal
634698	11	meal
634698	12	course
634698	13	course
634698	7	meal
88	11	meal
86	11	meal
97	11	meal
664643	11	meal
664643	12	course
664643	13	course
664643	7	meal
634854	26	dessert
645824	11	meal
645824	12	course
57	11	meal
645824	13	course
645824	7	meal
649034	11	meal
649034	12	course
649034	13	course
649034	7	meal
642125	19	course
642125	11	meal
50	1	cuisine
642125	12	course
642125	13	course
43	1	cuisine
53	1	cuisine
62	1	cuisine
30	1	cuisine
642125	7	meal
29	1	cuisine
636857	9	cuisine
39	1	cuisine
66	1	cuisine
636857	1	cuisine
50	2	cuisine
43	2	cuisine
67	2	cuisine
636857	22	course
50	3	course
62	3	course
636857	20	cuisine
39	3	course
636857	3	course
64	7	meal
636857	2	cuisine
636857	10	cuisine
57	12	course
97	12	course
96	12	course
46	12	course
96	13	course
86	13	course
97	13	course
88	13	course
92	13	course
89	13	course
96	16	cuisine
88	19	course
96	19	course
89	19	course
92	19	course
97	19	course
645694	19	course
662744	1	cuisine
662744	22	course
662744	20	cuisine
662744	3	course
662744	2	cuisine
662744	10	cuisine
659285	11	meal
659285	12	course
659285	13	course
659285	7	meal
660133	11	meal
660133	12	course
660133	13	course
660133	7	meal
631814	11	meal
631814	12	course
631814	13	course
631814	7	meal
715631	19	course
633324	11	meal
633324	12	course
62	2	cuisine
54	2	cuisine
29	2	cuisine
39	2	cuisine
633324	13	course
53	2	cuisine
30	2	cuisine
633324	7	meal
652061	19	course
54	3	course
67	3	course
66	3	course
29	3	course
652061	11	meal
30	3	course
53	3	course
43	3	course
652061	12	course
652061	13	course
89	7	meal
652061	7	meal
634404	19	course
634404	11	meal
634404	12	course
88	7	meal
68	7	meal
42	7	meal
634404	13	course
92	7	meal
634404	7	meal
664975	11	meal
664975	12	course
86	7	meal
664975	13	course
664975	7	meal
97	7	meal
75	7	meal
19	7	meal
96	7	meal
57	7	meal
646825	26	dessert
46	11	meal
19	11	meal
92	11	meal
75	11	meal
96	11	meal
89	11	meal
42	11	meal
92	12	course
86	12	course
64	12	course
88	12	course
68	12	course
75	12	course
42	12	course
89	12	course
46	13	course
64	13	course
54	9	cuisine
39	10	cuisine
50	10	cuisine
67	10	cuisine
43	10	cuisine
66	10	cuisine
30	10	cuisine
62	10	cuisine
\.


--
-- Data for Name: favorite_recipes; Type: TABLE DATA; Schema: public; Owner: atip
--

COPY public.favorite_recipes (user_id, recipe_id) FROM stdin;
8	26
8	647524
8	661570
1	715574
\.


--
-- Data for Name: ingredients; Type: TABLE DATA; Schema: public; Owner: atip
--

COPY public.ingredients (id, recipe_id, name, amount, unit) FROM stdin;
1394	645694	bacon	6	servings
1396	645694	duck breast fillets	6	servings
1397	645694	garlic powder	6	servings
1398	645694	newman's own dressing	6	servings
1467	649024	beef sirloin tips	2	pounds
1468	649024	garlic	1	Clove
1469	649024	green onions	10	
1470	649024	sesame oil	3	tablespoons
1471	649024	sesame seeds	3	tablespoons
1472	649024	soy sauce	0.25	cup
1473	649024	sugar	2	tablespoons
1583	715631	egg yolks	2	
1584	715631	eggs	2	large
1585	715631	lemon zest	2	tsp
1586	715631	lemons	2	large
1587	715631	salt	0.25	tsp
1588	715631	sugar	0.5	cup
1589	715631	butter	4	Tbsp
1655	645824	bell pepper	4	servings
1656	645824	clv garlic	1	
1657	645824	lime	1	
1658	645824	onion	1	small
1659	645824	sea salt	1	teaspoon
1660	645824	tiger prawns	1	pound
1661	645824	vegetable oil	1	teaspoon
1734	642125	rice	3	cups
1735	642125	eggs	3	
1736	642125	kaffir leaves	3	
1737	642125	curry paste	1	tablespoon
1738	642125	vegetables	1	cup
1739	642125	salt& pepper	4	servings
1787	645694	bacon	6	servings
1788	645694	pepper	6	servings
1789	645694	duck breast fillets	6	servings
1790	645694	garlic powder	6	servings
81	12	boquerones	12	
82	12	bell peppers	6	large
83	12	sherry vinegar	1	tablespoon
84	12	sugar	1	teaspoon
103	16	to 3 anchovy	2	fillet
104	16	thick diagonal baguette	16.5	inch
105	16	additional chives	1	serving
106	16	coarse kosher salt	1	serving
107	16	chives	2	Tbsps
108	16	radishes	10	
109	16	butter	0.5	cup
1399	647524	cream of mushroom soup	2	cans
1400	647524	onion	1	
1402	647524	salt and pepper	1	serving
1794	716346	d	1	d
133	19	anchovy	2	fillet
134	19	spoonfuls coarse cornmeal	3	
135	19	one-inch pinched fennel fronds	8	
136	19	fennel bulb	0.25	
137	19	spoonfuls flour	3	
138	19	lemon zest	1	tsp
139	19	mozzarella cheese	2	oz
140	19	olive oil	2	Tbsps
141	19	cracks pepper	3	
142	19	pizza dough	1	ball
189	25	anchovies	1	pound
190	25	eggs	3	large
191	25	flour	0.5	cup
192	25	garlic clove	1	
193	25	hungarian paprika	1.5	teaspoons
194	25	kosher salt	1	teaspoon
195	25	lemon juice	2	tablespoons
196	25	lemon wedges	8	servings
197	25	olive-oil mayonnaise	0.75	cup
198	25	panko bread crumbs)	1.75	cups
199	25	paprika	1.5	teaspoons
200	25	vegetable oil	8	servings
201	26	to 3 anchovy	2	fillet
202	26	thick diagonal baguette	16.5	inch
203	26	additional chives	16	servings
204	26	coarse kosher salt	16	servings
205	26	chives	2	Tbsps
206	26	radishes	10	
207	26	butter	0.5	cup
1403	665574	flour	4	ounces
1404	665574	salt	1	teaspoon
1405	665574	egg	1	
225	29	anchovy	20	fillet
226	29	pepper	4	servings
227	29	peppercorns	4	servings
228	29	capers	1	small handful
229	29	celery	2	stalks
230	29	chicory	2	heads
231	29	curly parsley tied together	1	bunch
232	29	curly parsley	1	handful
233	29	extra virgin olive oil	0.6666667	cup
234	29	fennel	1	head
235	29	garlic	1	head
236	29	garlic	8	cloves
237	29	lemon zest	1	
238	29	onion	1	
239	29	rocket	1	bunch
240	29	sea salt	4	servings
241	29	skate wing	1	
242	29	white wine	1	cup
243	29	a healthy red wine vinegar	1	tablespoon
244	30	anchovy	5	fillet
245	30	cubes country bread	3	cups
246	30	garlic cloves	3	
247	30	lemon juice	5	teaspoons
248	30	lemon juice	5	tsps
249	30	mustard greens	12	ounces
250	30	mustard greens	12	ozs
251	30	olive oil	0.5	cup
1406	665574	milk	1	pint
1407	665574	beef dripping	2	ounces
1590	633660	cream	2	tablespoons
1591	633660	eggs	4	
1592	633660	enough pastry to line flan tin	1	serving
1593	633660	extra lemon	1	
1594	633660	lemon juice	0.5	cup
1595	633660	rind of 1 lemon	1	medium
1596	633660	orange juice	0.5	cup
1597	633660	castor sugarl	1	cup
1662	652061	garlic	1	clove
1663	652061	heavy cream	1	tablespoon
1664	652061	miso paste	2	tablespoons
1665	652061	mushroom	1	cup
1666	652061	olive oil	1	serving
1667	652061	pasta	1	serving
1668	652061	onion	1	
1669	652061	shiso leaves	9	servings
1740	664975	ginger root	1	teaspoon
1408	649722	chuck arm steak	1.25	lbs
1409	649722	dill weed	0.25	teaspoon
314	37	anchovy	8	fillet
315	37	bread crumbs	1	cup
316	37	cauliflower	2	heads
317	37	extra virgin olive oil	0.25	cup
318	37	extra virgin olive oil	2	tablespoons
319	37	sage leaves	8	
320	37	garlic	3	cloves
321	37	kosher salt and pepper	3	servings
322	37	lemon zest	2	
323	37	shallot	1	
324	37	sugar	2	teaspoons
1410	649722	lemon juice	0.25	cup
1411	649722	cracked pepper	1	teaspoon
1412	649722	salt	36	servings
1413	649722	water	0.25	cup
1485	660133	chicken	1.2	kg
1486	660133	butter	0.5	stick
1487	660133	garlic	5	cloves
1488	660133	rind of two lemons	4	servings
1489	660133	chilli flakes	1	teaspoon
1490	660133	salt and pepper	4	servings
1491	660133	lemon	0.5	
336	39	anchovy	1	fillet
337	39	capers	1	tsp
338	39	flatleaf parsley	0.5	Tbsp
339	39	garlic clove	1	small
340	39	lemon juice	0.5	Tbsp
341	39	olive oil	1	Tbsp
342	39	radishes	1	large bunch
343	39	salt	4	servings
1492	660133	yukon gold potatoes	4	
1493	660133	sweet potatoes	2	
1494	660133	chilli flakes	1	pinch
1495	660133	olive oil	4	servings
1598	649230	brown sugar	1	cup
1599	649230	butter	0.25	cup
1600	649230	cinnamon	0.25	cup
1601	649230	apricots	0.25	cup
1602	649230	lamb riblets	2	pounds
362	42	anchovy	1	
363	42	bread	2	slices
364	42	butter	2	Tbsps
365	42	mozzarella	3	slices
366	42	garlic clove	0.5	small
367	42	kosher salt	1	pinch
368	42	lemon juice	0.5	tsp
369	42	olive oil	0.5	tsp
370	42	olives - half niçoise and half meaty/wrinkled olives	0.33333334	cup
371	42	sprig's worth of oregano leaves	1	
372	43	anchovies or	3	
373	43	olives	0.6666667	cup
374	43	pepper	0.5	teaspoon
375	43	capers	4	teaspoons
376	43	cherry tomatoes	0.5	pint
377	43	round crusty bread	12	ounce
378	43	parsley leaves	0.25	cup
379	43	garlic	2	cloves
380	43	hard-cooked eggs	6	
381	43	olive oil	0.25	cup
382	43	orange bell pepper	0.5	medium
383	43	onion	0.5	small
399	46	cauliflower	1	head
400	46	chicken stock	1.5	cups
401	46	pepper	1	teaspoon
402	46	flat-leaf parsley	0.5	cup
403	46	oil-packed anchovy	5	fillet
404	46	orecchiette	1	pound
405	46	parmesan cheese	0.5	cup
406	46	salt and pepper	6	servings
407	46	butter	4	ounces
408	46	pistachios	0.5	cup
1603	649230	lemon	1	
1604	649230	nutmeg	0.5	teaspoon
1605	649230	orange juice	0.5	cup
1606	649230	prunes	0.5	cup
1607	649230	salt	1	teaspoon
1608	649230	each	1	tablespoon
720	76	shallot	1	medium
416	48	anchovy	4	fillet
417	48	garlic	1	clove
418	48	olive oil	1	tablespoon
419	48	olive oil	1	Tbsp
420	48	bell peppers	14	ounces
421	48	bell peppers	14	ozs
1792	716344	d	1	d
429	50	anchovy fillets	3	large
430	50	brioche	0.75	cup
431	50	eggs	10	large
432	50	garlic	0.5	teaspoon
433	50	lemon zest	0.5	teaspoon
434	50	mayonnaise	0.25	cup
435	50	parsley	1	tablespoon
436	50	butter	1	tablespoon
1414	654485	add-ins - i used of bacon fbatch of 12 pancake bites	4	slices
1415	654485	butter	0.5	cup
1416	654485	maple syrup	0.75	cup
1417	654485	pancake batter	3.5	c
1496	658136	beef chuck	3	pounds
1497	658136	ginger	1	tablespoon
1498	658136	cubes	2	servings
1499	658136	scallions	2	
1500	658136	sherry	1	cup
1501	658136	whl star anise	1	
1502	658136	sugar	1	teaspoon
1503	658136	vegetable oil	1	tablespoon
1609	632117	almonds	1	cup
1610	632117	brandy	2	tablespoons
1611	632117	butter	1	cup
1612	632117	cinnamon	0.5	tablespoon
1613	632117	egg	1	
463	53	marinated anchovy	12	fillet
464	53	curly parsley	3	Tbsps
465	53	dijon vinaigrette	0.25	cup
466	53	kosher salt and pepper	4	servings
467	53	little gem lettuce	4	ozs
468	53	olive oil	1.5	Tbsps
469	53	tomatoes on the vine	1.3333334	lbs
470	54	anchovies	6	
471	54	thick tuscan bread	6.5	inch
472	54	caperberries	12	
473	54	garlic clove	1	large
474	54	olive oil	6	servings
475	54	piquillo peppers	8	ounce
476	54	sea salt and pepper	6	servings
1614	632117	lemon	0.5	
1615	632117	rind	1	serving
1616	632117	nutmeg	1	serving
1617	632117	flour	100	g
1618	632117	sugar	0.5	cup
1619	632117	each	0.5	tablespoon
1670	654886	angel hair	1	pound
1671	654886	balsamic vinegar	1	teaspoon
1672	654886	basil leaves	3	
1673	654886	olive oil	1.5	tablespoons
1674	654886	bell pepper	1	
1675	654886	salt and cracked pepper	1	serving
1676	654886	onion	1	small
1677	654886	tomatoes	14	ounces
1741	664975	honey	2	tablespoons
1742	664975	soy sauce	1	tablespoon
1743	664975	mirin	3	tablespoons
494	57	anchovy	12	fillet
495	57	pork loin roast	2.5	pound
496	57	flour	1	tablespoon
497	57	garlic cloves	6	
498	57	lemon juice	0.25	cup
499	57	lemon zest	2	tablespoons
500	57	olive oil	1	tablespoon
501	57	ruby port	1	cup
502	57	prunes	5	ounces
503	57	salt and pepper	6	servings
1744	664975	rice vinegar	1	tablespoon
1745	664975	salmon fillets	12	ounces
1746	664975	wasabi paste	4	teaspoons
521	60	broccoli	3	pounds
522	60	lemon juice	0.33333334	cup
523	60	oil-packed anchovy	12	fillet
524	60	olive oil	0.5	cup
525	60	rosemary	1	teaspoon
526	60	salt and pepper	6	servings
1793	716345	d	1	d
537	62	anchovy paste	1	teaspoon
538	62	avocado	1	
539	62	pepper	6	servings
540	62	croutons	6	servings
541	62	dijon mustard	0.5	teaspoon
542	62	garlic cloves	1	
543	62	lemon juice	2	Tablespoons
544	62	a wedge into strips	0.25	cup
545	62	romaine lettuce	1	head
546	62	sea salt	0.5	teaspoon
547	62	water	6	Tablespoons
548	62	unrefined	3	Tablespoons
563	64	anchovy fillets	6	large
564	64	wine	0.25	cup
565	64	garlic cloves	3	large
566	64	greek olives	18	
567	64	lemon juice	1	tablespoon
568	64	olive oil	0.25	cup
569	64	salt and pepper	6	servings
570	64	scallions	4	large
571	64	shrimp	1.75	pounds
572	64	butter	1	tablespoon
585	66	marinated anchovy	16	fillet
586	66	in. length of baguette	2	
587	66	chive pieces	2	tablespoons
588	66	eggs	4	extra large
589	66	flat-leaf parsley	2	tablespoons
590	66	lemon	1	
591	66	olive oil	2	tablespoons
592	66	bell pepper	8	servings
593	66	sea salt	8	servings
594	67	tiny cherry tomatoes	36	
595	67	cucumber —peeled	0.75	pound
596	67	feta cheese	0.5	pound
597	67	garlic clove	1	
598	67	mayonnaise	0.5	cup
599	67	oil-packed anchovy	2	fillet
600	67	olive oil	2	tablespoons
601	67	red wine vinegar	2	tablespoons
602	68	pepper	0.25	teaspoon
603	68	anchovy	3	fillet
604	68	pepper	0.5	teaspoon
605	68	olive oil	1	tablespoon
606	68	less-sodium chicken broth	0.5	cup
607	68	parsley	1	tablespoon
608	68	garlic	1.5	teaspoons
609	68	bread	1	ounce
610	68	parmesan cheese	2	ounces
611	68	salt	0.5	teaspoon
612	68	spaghetti	1	pound
673	71	anchovy fillets	8	large
674	71	bread crumbs	2	cups
675	71	cayenne pepper	0.25	teaspoon
676	71	eggs	2	large
677	71	flour	0.5	cup
678	71	tomatoes	3	pound
679	71	kosher salt	0.5	teaspoon
680	71	lemon wedges	8	servings
681	71	olive oil	0.5	cup
682	71	water	2	tablespoons
704	75	anchovy	6	fillet
705	75	nonpareil capers	0.5	cup
706	75	pepper	0.5	teaspoon
707	75	flat-leaf parsley	0.5	cup
708	75	garlic clove	1	
709	75	lemon juice	2	tablespoons
710	75	lemon zest	1	tablespoon
711	75	olive oil	0.33333334	cup
712	75	olive oil	0.33333334	cup
713	75	spaghetti	1	pound
714	76	marinated anchovies	12	
715	76	belgian endives	2	large
716	76	garlic clove	1	
717	76	olive oil	1	tablespoon
718	76	pita breads	2	6-inch
719	76	salt and pepper	4	servings
721	76	cream	0.75	cup
722	76	butter	4	tablespoons
723	76	balsamic vinegar	1.5	tablespoons
1362	633338	beef tenderloin steaks	4	inches
1363	633338	bacon	4	slices
1364	633338	garlic	2	large cloves
1365	633338	salt& pepper	4	servings
1418	662744	ground beef	1	lb
1419	662744	taco seasoning	1	package
745	79	anchovy	4	fillet
746	79	globe artichokes	8	medium
747	79	flat-leaf parsley	0.25	cup
748	79	fleur de sel	8	servings
749	79	garlic cloves	2	
750	79	ground pepper	1	teaspoon
751	79	kosher salt	8	servings
752	79	lemon juice	1	tablespoon
753	79	to 4 lemons	3	
754	79	butter	4	ounces
755	79	vegetable oil	0.25	cup
756	80	pepper	0.25	teaspoon
757	80	garlic	1	large clove
758	80	kosher salt	0.5	teaspoon
759	80	olive oil	5	tablespoons
760	80	oregano	8	sprigs
761	80	radicchio	2	heads
762	80	red wine vinegar	2	tablespoons
813	86	pepper	0.25	teaspoon
814	86	capers	1.5	tablespoons
815	86	kalamata olives	0.75	cup
816	86	linguine	1	pound
817	86	marinara sauce	26	ounce
818	86	olive oil	1.5	tablespoons
819	86	shrimp	1	pound
1420	662744	egg roll wrappers	8	
1421	662744	mexican cheese	1	package
1504	645710	butter	2	T
1505	645710	another fish	1.5	lb
1506	645710	parsley	1.5	T
1507	645710	garlic clove	1	
1508	645710	hamburger buns	4	
1509	645710	lemon juice	2	T
1510	645710	mayonnaise	0.5	c
1511	645710	toppings: such as pickles	4	servings
1512	645710	salt	0.5	teaspoon
1513	645710	salt & pepper	4	servings
1514	645710	paprika	0.5	t
1515	645710	vegetable oil	4	servings
1516	645710	mustard	0.75	t
1620	663175	basil leaves	2	tablespoons
1621	663175	cayenne	0.25	teaspoon
831	88	anchovies	4	ounces
832	88	chives	2	tablespoons
833	88	coarse sea salt	6	servings
834	88	pepper	0.25	teaspoon
835	88	garlic cloves	4	large
836	88	parmesan cheese and lemon wedges	6	servings
837	88	mint	0.25	cup
838	88	olive oil	0.25	cup
839	88	pappardelle	1	pound
840	88	zucchini	1.5	pounds
841	89	eggs	4	
842	89	warm milk	0.5	cup
843	89	olive oil	6	tablespoons
844	89	onion	1	medium
845	89	parsley	2	bunches
846	89	anchovies	8	
847	89	flour	4	cups
864	92	bucatini pasta	1	pound
865	92	anchovy fillets	4	ounce
866	92	garlic cloves	7	
867	92	bread	3	cups
868	92	olive oil	8	tablespoons
869	92	parmigiano-reggiano	0.5	cup
870	92	parsley leaves	0.33333334	cup
871	92	chili flakes	0.5	teaspoon
872	92	roasted bell peppers	1	cup
873	92	salt	4	servings
874	92	onion	1	cup
891	96	peasant bread	6	slices
892	96	capers	2	tablespoons
893	96	garlic clove	1	large
894	96	log goat cheese	0.5	pound
895	96	oil-packed anchovy	6	fillet
896	96	olive oil	2	tablespoons
897	96	cracked sicilian olives	10	
898	96	bell peppers	2	large
899	96	red wine vinegar	1	tablespoon
900	96	rosemary	1	teaspoon
901	96	bell peppers	2	large
902	97	anchovy	4	fillet
903	97	bay leaves	2	
904	97	edam cheese	8	ozs
905	97	flour	0.33333334	cup
906	97	basil leaves	0.5	cup
907	97	flat-leaf parsley	0.5	cup
908	97	garlic	5	cloves
909	97	manchego cheese	6	ozs
910	97	mozzarella cheese	4	ozs
911	97	nutmeg	0.25	tsp
912	97	olive oil	0.25	cup
913	97	parmigiano-reggiano cheese	1	cup
914	97	penne rigate	1	lb
915	97	sea salt and pepper	8	servings
916	97	milk	7	cups
1517	664643	water	1	cup
1518	664643	salt	1	teaspoon
1519	664643	bulgur	1	cup
1520	664643	lrgs carrots	2	
1521	664643	tofu	4	ounces
1522	664643	egg white	1	
1523	664643	mint	3	tablespoons
1524	664643	scallions	3	tablespoons
1525	664643	cayenne pepper	1	teaspoon
1526	664643	bread crumbs	1	cup
1527	664643	flour	1	cup
1528	664643	ketchup	2	tablespoons
1529	664643	dijon mustard	2	teaspoons
1366	716342	suya spice	1.5	Tablespoons
1367	716342	chicken	1	pound
1368	716342	chilli powder	1	teaspoon
1369	716342	cooking spoon groundnut oil	1	
1370	716342	seasoning cubes	1	serving
1371	716342	onions and tomatoes	1	serving
1372	716342	salt	1	serving
1422	643829	ground beef/pork	0.5	pound
1423	643829	cabbage	2	cups
1424	643829	water chestnuts	2	cups
1425	643829	salt	1	serving
1426	643829	vegetable oil enough	1	serving
1427	643829	wonton wrappers	1	pkg
1530	664643	olive oil	1	tablespoon
1531	664643	hamburger buns	4	
1532	664643	romaine lettuce leaves	4	
1533	664643	lrgs tomato	4	
1534	664643	tomato	12	slices
1535	664643	alfalfa sprouts	1	cup
1622	663175	fish	4	servings
1623	663175	garlic	4	Cloves
1624	663175	ginger	1	teaspoon
1625	663175	green onions	6	
1626	663175	salt and pepper	4	servings
1627	663175	sesame oil	1	teaspoon
1678	655806	farfalle	0.5	lb
1679	655806	flat leaf parsley	1.5	cups
1680	655806	garlic	3	cloves
1681	655806	yogurt	0.25	cup
1682	655806	nuts	0.25	cup
1683	655806	olive oil	2	tablespoons
1684	655806	parmesan cheese	0.25	cup
1685	655806	salt & pepper	4	servings
1747	654435	pepper	0.25	teaspoon
1748	654435	dill	1	tbsp
1749	654435	garlic clove	1	
1750	654435	lemon juice	1	tbsp
1751	654435	lemon wedges	2	servings
1752	654435	olive oil	0.25	cup
1753	654435	salmon fillets	12	oz
1754	654435	salt	0.125	teaspoon
1373	645694	bacon	6	servings
1374	645694	pepper	6	servings
1375	645694	duck breast fillets	6	servings
1376	645694	garlic powder	6	servings
1377	645694	newman's own dressing	6	servings
1428	645879	half a spring chicken	1	
1429	645879	honey	0.25	cup
1430	645879	honey	2	teaspoons
1431	645879	salt & pepper	1	serving
1432	645879	sesame oil	1	tablespoon
1433	645879	sesame oil	1	teaspoon
1434	645879	sesame seeds	2	teaspoons
1435	645879	soy sauce	1	tablespoon
1436	645879	soy sauce	1	tablespoon
1536	631814	pre-washed bagged baby arugula	1.5	cups
1537	631814	regular bacon	4	slices
1538	631814	drain off the bacon fat from the skillet	4	servings
1539	631814	balsamic vinegar	2	tablespoons
1540	631814	combine the chuck	2	
1541	631814	fennel bulbs	1	medium
1542	631814	basil leaves	3	tablespoons
1543	631814	figs	4	
1544	631814	garlic cloves	1	
1545	631814	ground turkey	0.5	pound
1546	631814	hamburger buns	2	
1547	631814	aged teleme cheese thinly 2 • hamburger buns	2	ounces
1548	631814	prepare a medium-hot fire in a charcoal grill	4	servings
1549	631814	lemons	0.5	
1550	631814	olive oil	0.5	tablespoon
1551	631814	olive oil	2	tablespoons
1552	631814	onion	2	tablespoons
1553	631814	salt	1	pinch
1554	631814	salt	4	servings
1555	631814	salt	4	servings
1556	631814	sun-dried tomatoes	3	tablespoons
1557	631814	to assemble the burgers	1	servings
1558	631814	vegetable oil	3	tablespoons
1559	631814	walnuts	4	tablespoons
1560	631814	heat a	1	large
1686	649034	beef flank steak	1	pound
1687	649034	pepper	1	serving
1688	649034	chives	1	tablespoon
1689	649034	bell pepper	1	serving
1690	649034	ginger	1	tablespoon
1691	649034	garlic	2	cloves
1692	649034	salt	1	serving
1693	649034	sesame oil	0.25	cup
1694	649034	soy sauce	1	tablespoon
1695	649034	rice	2	cups
1755	655130	sponge cake	1	
1756	655130	brandy	4	tablespoons
1757	655130	peach halves	8	
1758	655130	vanilla ice-cream	4	scoops
1759	655130	whipped cream	100	servings
1760	655130	almonds	1	tablespoon
1761	655130	raspberries	1	cup
1762	655130	sugar	4	teaspoons
1763	655130	lemon juice	1	teaspoon
1378	647524	cream of mushroom soup	2	cans
1379	647524	onion	1	
1380	647524	rump beef roast	5	pounds
1437	634698	beef	0.75	pound
1438	634698	japanese cucumber	1	
1439	634698	daikon	7	ounces
1440	634698	ginger	2	teaspoons
1441	634698	garlic	5	cloves
1442	634698	lemon	1	
1443	634698	shiso leaves	4	servings
1444	634698	soy sauce	4	servings
1561	715574	strawberries	10	large
1562	715574	vanilla ice cream	2.5	cups
1563	715574	milk	2	cups
1634	633324	bacon	10	slices
1635	633324	sea scallops	20	large
1636	633324	whipping cream	1	cup
1637	633324	dijon mustard	2	tablespoons
1638	633324	maple syrup	2	tablespoons
1639	633324	chives	4	servings
1696	634404	butter	1	Tbs
1697	634404	olive oil	1	Tbs
1698	634404	arborio rice	1	cup
1699	634404	garlic cloves	2	
1700	634404	shallot	1	
1701	634404	flat leaf parsley	2	Tbs
1702	634404	chicken stock - heated	3	cups
1703	634404	parmesan cheese	4	tablespoons
1704	634404	salt and pepper	2	servings
1705	634404	inch suggested optional items to add -mushrooms	1	inch
1764	636857	brown sugar	0.75	cup
1765	636857	butter	4	tablespoons
1766	636857	cinnamon	0.5	teaspoon
1767	636857	egg whites	4	
1768	636857	nutmeg	0.25	teaspoon
1769	636857	pecans	2	pounds
1770	636857	salt	0.25	teaspoon
1771	636857	vanilla	1	teaspoon
1382	665574	flour	4	ounces
1383	665574	salt	1	teaspoon
1384	665574	egg	1	
1385	665574	milk	1	pint
1386	665574	beef dripping	2	ounces
1445	659285	bread	2	slices
1446	659285	glove garlic	1	
1447	659285	ginger	1	tsp
1448	659285	ground beef	400	g
1449	659285	parsley	1	tbsp
1450	659285	peanut butter	3	tbsp
1451	659285	soya sauce	2	tbsp
1452	659285	spring onion	2	
1564	632629	all purpose flour	1.5	cups
1565	632629	winsap apples	6	large
1566	632629	tbsp. butter	0.5	pound
1567	632629	butter	1	teaspoon
1568	632629	cinnamon	1	teaspoon
1569	632629	granulated sugar	0.75	cup
1570	632629	lemon juice	2	tablespoons
1571	632629	brown sugar	0.75	cup
1572	632629	nutmeg	1	teaspoon
1573	632629	oatmeal	0.5	cup
1574	632629	walnuts	1	cup
1575	632629	water	0.25	cup
1640	644357	.3lb tiger prawns	600	gr
1641	644357	olive oil	1	tbsp
1642	644357	garlic cloves thinly	6	large
1643	644357	shallot	4	servings
1644	644357	the of 3	1	leaves
1645	644357	course sea salt	1	tsp
1646	644357	juice of lemon	1	
1647	644357	pepper	4	servings
1706	632797	rice	3	cups
1707	632797	cornstarch	1	tablespoon
1708	632797	ginger	1	tablespoon
1709	632797	bell pepper	1	
1710	632797	pineapple chunks	20	ounces
1711	632797	soy sauce	2	tablespoons
1712	632797	sugar	1	teaspoon
1713	632797	vegetable oil	2	teaspoons
1772	646825	flour	3	cups
1773	646825	walnuts - ground in food processor	1	cup
1774	646825	baking powder	1	tsp
1775	646825	sugar	1	cup
1776	646825	butter	0.75	cup
1777	646825	eggs	2	
1778	646825	vanilla	1	tsp
1779	646825	cherry gelatin	1.4	oz
1324	96	peasant bread	6	slices
1325	96	capers	2	tablespoons
1326	96	garlic clove	1	large
1327	96	log goat cheese	0.5	pound
1328	96	oil-packed anchovy	6	fillet
1329	96	olive oil	2	tablespoons
1330	96	cracked sicilian olives	10	
1331	96	bell peppers	2	large
1332	96	red wine vinegar	1	tablespoon
1333	96	rosemary	1	teaspoon
1334	96	bell peppers	2	large
1335	97	anchovy	4	fillet
1336	97	bay leaves	2	
1337	97	edam cheese	8	ozs
1338	97	flour	0.33333334	cup
1339	97	basil leaves	0.5	cup
1340	97	flat-leaf parsley	0.5	cup
1341	97	garlic	5	cloves
1342	97	manchego cheese	6	ozs
1343	97	mozzarella cheese	4	ozs
1344	97	nutmeg	0.25	tsp
1345	97	olive oil	0.25	cup
1346	97	parmigiano-reggiano cheese	1	cup
1347	97	penne rigate	1	lb
1348	97	sea salt and pepper	8	servings
1349	97	milk	7	cups
1387	716342	suya spice	1.5	Tablespoons
1388	716342	chicken	1	pound
1389	716342	chilli powder	1	teaspoon
1390	716342	cooking spoon groundnut oil	1	
1391	716342	seasoning cubes	1	serving
1392	716342	onions and tomatoes	1	serving
1393	716342	salt	1	serving
1453	716300	beef	1	cup
1454	716300	bell pepper	1	
1455	716300	bell peppers	1	handful
1456	716300	bread flour	2	cups
1457	716300	seasoning cube	3	servings
1458	716300	oil	1	tablespoon
1459	716300	oil	1	teaspoon
1460	716300	onions	1	handful
1461	716300	over-ripe plantain	1	
1462	716300	salt	1	teaspoon
1463	716300	sugar	0.5	teaspoon
1464	716300	tomato)	1	
1465	716300	water	0.75	cup
1466	716300	yeast	1.5	teaspoons
1576	634854	berries	4	cups
1577	634854	maple syrup	1	Tablespoon
1578	634854	old fashion oatmeal	0.33333334	cups
1579	634854	almond meal	0.33333334	cups
1580	634854	brown sugar	4	teaspoons
1581	634854	ground cinnamon	1	teaspoon
1582	634854	margarine	7	teaspoons
1648	661570	halibut steaks	2	pounds
1649	661570	soy sauce	2.5	tablespoons
1650	661570	sesame oil	1.5	teaspoons
1651	661570	pepper	0.125	teaspoon
1652	661570	ginger	3	tablespoons
1653	661570	scallions	0.25	cup
1654	661570	cilantro	1	handful
1714	641559	baby spinach	3	cups
1715	641559	bean sprouts	1.5	cups
1716	641559	bulgogi beef	0.75	pound
1717	641559	dolsot stone bowls	4	
1718	641559	cabbage kimchi	10	ounces
1719	641559	carrots	1	cup
1720	641559	egg yolks	4	
1721	641559	shiitake mushrooms	1	cup
1722	641559	garlic clove	1	
1723	641559	green onions	1	cup
1724	641559	korean barbecue bulgogi marinade	1	cup
1725	641559	kochujang vinegared pepper paste	0.25	cup
1726	641559	salt	1	pinch
1727	641559	sesame oil	0.25	cup
1728	641559	sesame seeds	2	teaspoons
1729	641559	short grain rice	4	cups
1730	641559	sugar	1	pinch
1731	641559	high grade korean sushi rice	3	cups
1732	641559	tofu	0.75	cup
1733	641559	zucchini	1	cup
1780	716342	suya spice	1.5	Tablespoons
1781	716342	chicken	1	pound
1782	716342	chilli powder	1	teaspoon
1783	716342	cooking spoon groundnut oil	1	
1784	716342	seasoning cubes	1	serving
1785	716342	onions and tomatoes	1	serving
1786	716342	salt	1	serving
\.


--
-- Data for Name: instructions; Type: TABLE DATA; Schema: public; Owner: atip
--

COPY public.instructions (id, recipe_id, step, detail) FROM stdin;
34	16	1	Mix butter, 2 chopped anchovy fillets, and 2 tablespoons chives in small bowl, adding 1 more chopped anchovy fillet to taste, if desired. Season with salt and freshly ground black pepper.
35	16	2	Spread anchovy butter over 1 side of each baguette slice. Top each baguette slice with radish slices, overlapping slightly to cover bread.
36	16	3	Garnish with additional chopped chives and serve.
27	12	1	Preheat broiler.
28	12	2	Broil bell peppers on a broiler pan about 5 inches from heat, turning occasionally with tongs, until skins are blackened, 15 to 20 minutes.
29	12	3	Transfer to a large bowl and cover bowl tightly with plastic wrap, then let steam 20 minutes.
30	12	4	When peppers are cool enough to handle, peel them, reserving all juices in bowl, and discard stems and seeds.
31	12	5	Cut peppers lengthwise into 1/4-inch-wide strips.
32	12	6	Pour pepper juices through a sieve into another bowl, then add vinegar and sugar to juices, stirring until sugar is dissolved, then stir in peppers. Marinate peppers at room temperature, stirring occasionally, at least 2 hours.
33	12	7	Spoon peppers and juices into a shallow bowl and arrange anchovy strips decoratively on top.
46	19	1	Preheat oven to 500 F. If you have a pizza stone, stick it in the oven.In a small skillet, heat 1 tablespoon olive oil over medium heat.
47	19	2	Add fennel slices and cook, stirring occasionally, until slightly browned.
48	19	3	Remove from heat.With floured hands over a floured surface, stretch or toss (if you know how) the dough until it is 10-12", taking care not to stretch it too thin. Uneven is okay, this dough makes a rustic crust. No need to aim for a perfect circle either. Press small thumbprints around the crust and brush with remaining tablespoon olive oil.
49	19	4	Sprinkle a baking sheet with cornmeal and transfer the crust over. Re-shape if it's gone askew. Top with the mozzarella slices, fennel, and anchovy. Slide onto the pizza stone, or place baking sheet in oven.Cook until crust looks golden brown and cheese is bubbling, 6-10 minutes. When ready, carefully pull from the oven, top with lemon zest, a few cracks of pepper and the fennel fronds. Slice and serve. For the No-Knead Pizza Dough recipe and the story behind it, see the Tasting
50	19	5	Table.com article, Jim Lahey Reveals His Recipe for No-Knead Pizza Dough No time to wait for No-Knead?
51	19	6	Roll your sleeves up and try our recipe for Homemade Thin Crust Pizza
52	19	7	Pin itLast Week's Posted Email: On Making Your Own Pasta
53	19	8	Show Nutritionbalancedsugar-conscious
54	19	9	Per serving, based on2servings.(% daily value)Calories541Fat26.2 g(40.3%)Saturated8.3 g(41.7%)Carbs58 g(19.3%)Fiber3.2 g(12.7%)Sugars1.3 gProtein17.7 g(35.4%)Cholesterol31.5 mg(10.5%)Sodium813.2 mg(33.9%)
55	25	1	Stir mayonnaise, lemon juice, garlic, and paprikas together in a bowl. Chill aioli until serving.
56	25	2	Clean fish (steps 1 and 2 of "You Found the Fish," below).
57	25	3	Preheat oven to 20
58	25	4	Line a rimmed baking sheet with paper towels and keep warm in oven. Fill a large pot with 1 in. oil, insert a deep-fry thermometer, and bring oil to 375 over medium-high heat.
59	25	5	Combine flour and 1/2 tsp. salt in a pie pan, and panko and remaining 1/2 tsp. salt in another pie pan. In a shallow bowl, whisk eggs to blend. Dip fish in flour, shaking off excess, then in egg, then in panko, turning to coat; set on a baking sheet.
60	25	6	Fry one-quarter of fish at a time until golden, 1 to 1 1/2 minutes.
61	25	7	Transfer to pan in oven.
62	25	8	Serve with aioli and lemon wedges.
63	25	9	You Found the Fish--Now What? Some markets will clean them for you, but if not, you can do it yourself easily enough--it just takes a little practice.
64	25	10	SCALE AND CUT. Scrape off the scales gently with fingertips.
65	25	11	Cut through both sides of belly 1/4 in. from edge, from collar to tail.
66	25	12	CLEAN. Pull out the guts; rinse the fish inside and out. Snip off fins.
67	25	13	FILLET (RAW). Score fish all the way around collar just to the bone. Slide your index finger into cut on one side of collar and your middle finger into the other side. Slide your fingers along spine to tail, pulling fillets free.
68	25	14	Cut off tail and pull out any remaining bones.
69	25	15	FILLET (COOKED). Make 3 cuts through flesh to bones: along the length of the spine (to one side of it), at collar, and just above tail. Slide knife under fillet to free it from spine, and lift it off. Pull up tail and lift off spine and head to free bottom fillet. Pull out any remaining bones.
70	25	16	*If you can't find fresh anchovies or smelt, you can make the recipe with sardines: Discard heads and tails, and cut bodies into 2-in. pieces.
71	25	17	Cut cooked meat from the bones.
72	25	18	Note: Find these little fish at some grocery stores, fish markets (you might need to order them), and Asian markets. If you live near a coastal town, head to the docks-fresh anchovies and smelt are often sold as bait. Look for fish with bright eyes, shiny skin, and a mild aroma. They're very perishable, so plan to cook them the same day.
73	26	1	Mix butter, 2 chopped anchovy fillets, and 2 tablespoons chives in small bowl, adding 1 more chopped anchovy fillet to taste, if desired. Season with salt and freshly ground black pepper.
74	26	2	Spread anchovy butter over 1 side of each baguette slice. Top each baguette slice with radish slices, overlapping slightly to cover bread.
75	26	3	Garnish with additional chopped chives and serve.
76	26	4	89 calories, 6 g fat, 0.4 g fiber
87	29	1	To make your poaching broth mix all the ingredients together and add enough water to cover your skate. Bring it up to a boil and then turn the heat down to a simmer. Slip your skate wing into the poaching pan and cook for approximately 10 minutes (check that the flesh comes away from the bone), then turn off the heat and allow to cool in the liquor.
88	29	2	When cold remove the skate from the liquor and pull the flesh from the bone. It should come away in easy strips. Now make your dressing: either whizz all the ingredients in a food processor or pound them in a mortar with a pestle.
89	29	3	Bring together the skate, chicory, rocket (arugula), parsley, capers, and the dressing (cautionthere may be too much, so do not add it all at once), and toss.
90	29	4	var article
91	29	5	Type_27_data = {};
92	29	6	article
93	29	7	Type_27_data.init_step_by_step_images = 0;
94	30	1	Preheat oven to 375F.
95	30	2	Combine anchovies and garlic in small bowl. Gradually whisk in oil.
96	30	3	Place bread cubes in medium bowl.
97	30	4	Drizzle 2 tablespoons anchovy oil over, tossing to coat.
98	30	5	Sprinkle bread with salt, pepper, and half of cheese; toss to coat.
99	30	6	Spray rimmed baking sheet with nonstick spray. Scatter bread on sheet.
100	30	7	Bake croutons until crisp and golden, stirring occasionally, about 20 minutes. Set aside.
101	30	8	Measure 8 cups (loosely packed) mustard greens and place in large bowl (reserve any remaining greens for another use).
102	30	9	Add croutons and remaining cheese to bowl.
103	30	10	Whisk 5 teaspoons lemon juice into remaining anchovy oil; season dressing with salt, pepper, and more lemon juice, if desired.
104	30	11	Add dressing to salad; toss to coat.
106	37	1	Preheat oven to 400 degrees. Break cauliflower into florets and toss in a bowl with sage, lemon zest, sugar and olive oil. Season with salt and pepper and spread out on a large baking sheet.
107	37	2	Place in oven and cook until tender and golden, approximately 20 to 25 minutes. Meanwhile, prepare bread crumbs.
108	37	3	Heat olive oil in a saut pan set over medium heat. When oil shimmers, add the anchovies, garlic, shallot and bread crumbs. Cook for 5 to 7 minutes, until golden. In a large bowl, toss together cauliflower and bread crumbs and serve on a warmed platter.  Be sure to try out these other Thanksgiving recipes on Food Republic:  Pecan, Bourbon And Cane Syrup Ham Recipe Country Ham And Cheese Biscuit Bread Classic Giblet Gravy Recipe
113	39	1	Trim tops and tails from the radishes. Scrub them well. Slice each radish into 4 wedges (if small) or 6 wedges (if large).
114	39	2	With a mortar and pestle (or in a mini food processor), mash the anchovy, garlic, and a pinch of salt to a paste.
115	39	3	Mix in the lemon juice, then slowly blend in the oil, adding it in a thread-thin stream as you mix. Fold in the capers.
116	39	4	Add the sauce and parsley to the radishes and fold until well blended. Adjust lemon juice and salt to taste.
117	39	5	Serve within 30 minutes.
120	42	1	Mince the garlic.
121	42	2	Add the salt and keep mincing until the garlic forms a paste.
122	42	3	Place the olives and anchovy on your cutting board and coarsely chop them all together until fine but not completely paste-like.
123	42	4	Transfer to a small bowl and add the lemon juice and olive oil.On one side of the bread, place the mozzarella.
124	42	5	Sprinkle with oregano. On the other, mound most the tapenadethe amount depends on the size of your bread and your appetite for olives. Melt half the butter in a frying pan over medium-low heat.
125	42	6	Place the sandwich in the pan with a weight on top for best results. Cook for 5-6 minutes, until the bread is golden and the cheese starts to melt. Lift the sandwich up, add the rest of the butter, flip the sandwich, and cook about 5 minutes on the second side.
126	42	7	Cut in half and serve.
127	43	1	Hollow out the bread by removing most of the inside crumb. Reserve 1/2 cup of the crumb for the filling.
128	43	2	Place the olive oil, capers,parsley, garlic, pepper, and anchovies (or salt) in a food processor. Process until the garlic is finely chopped, 1 to 2 minutes.
129	43	3	Transfer the mixture to a large bowl.
130	43	4	Add the bell pepper,tomatoes, onion, olives, and the reserved bread filling. Toss to combine.
131	43	5	Layer half the mixture in the bottom half of the hollowed-out bread. Top with the hard-cooked eggs and the remaining mixture. Replace the top of the loaf. Wrap the filled loaf with plastic wrap. Weigh it down with a heavy object, such as a cast-iron skillet filled with cans.
132	43	6	Place it in the refrigerator.
133	43	7	Let sit at least 10 hours or overnight. Before serving, cut the loaf into 6 wedges with a sharp bread knife.
134	46	1	Preheat the oven to 35
135	46	2	Spread the pistachios in a pie plate and bake for about 5 minutes, or until lightly toasted.
136	46	3	Let cool, then coarsely chop.
137	46	4	In a medium saucepan of boiling water, blanch the cauliflower florets for 1 minute.
138	46	5	Drain and set aside.
139	46	6	In a large, deep skillet, cook the butter over moderate heat until golden brown, about 4 minutes.
140	46	7	Add the cauliflower and cook over moderately high heat until golden.
141	46	8	Add the anchovies and cook, stirring, for 2 minutes. Stir in the stock and cook until the cauliflower is tender, about 3 minutes.
142	46	9	Meanwhile, in a large pot of boiling salted water, cook the orecchiette until al dente.
143	46	10	Drain the pasta and add it to the skillet. Stir in the parsley, Parmesan and crushed red pepper and season with salt and pepper.
144	46	11	Transfer to a warmed bowl, sprinkle with the chopped pistachios and serve.
152	48	1	Transfer peppers to a large bowl, and cover immediately with plastic wrap. Set aside to steam, about 15 minutes. Peel peppers; discard skins.
153	48	2	Remove stems, seeds, and ribs, and cut each pepper lengthwise into 8 strips.
154	48	3	Transfer to a small non-reactive bowl.
155	50	1	Preheat the oven to 350 In a large saucepan, cover the eggs with water and bring to a simmer. Cook over moderate heat for 8 minutes.
156	50	2	Drain the eggs, return them to the pan and shake the pan to crack the shells all over. Fill the pan with cold water and let the eggs cool for 3 minutes.
157	50	3	Drain and peel the eggs; pat dry.
158	50	4	Meanwhile, in a small bowl, blend together the mayonnaise, garlic and one-third of the minced anchovies.
159	50	5	In a small skillet, melt the butter over moderate heat.
160	50	6	Add the remaining minced anchovies and cook, stirring, until they break down, about 1 minute. Stir in lemon zest and brioche crumbs and transfer to a rimmed baking sheet.
161	50	7	Bake the crumbs until golden brown and crisp, about 2 minutes.
162	50	8	Halve the eggs and arrange on a platter. Dollop 1/4 teaspoon of the mayonnaise on each egg yolk. Top each with the anchovy crumbs and parsley and serve.
163	53	1	Preheat oven to 40
164	53	2	Place tomatoes in an 8x8x2" glass baking dish. Season with salt and pepper, then drizzle with oil. Roast tomatoes until softened, about 30 minutes.
165	53	3	Let cool.
166	53	4	Transfer tomatoes to a large bowl, leaving juices behind.
167	53	5	Pour vinaigrette into baking dish and whisk into the tomato juices to blend.
168	53	6	Add anchovies and lettuce to bowl with tomatoes.
169	53	7	Drizzle vinaigrette over. Toss salad to coat (it's best if you use your hands). Season salad to taste with salt and pepper.
170	53	8	Sprinkle parsley over and serve.
171	54	1	Preheat the broiler. Toast the bread until golden, then lightly brush with olive oil. Rub the toasts on 1 side with the garlic clove. In a small bowl, toss the piquillos with the anchovies and caperberries. Spoon the topping on the toasts.
172	54	2	Drizzle with olive oil, sprinkle with salt and pepper and serve.
178	57	1	In a small saucepan, cover the prunes with the port and bring to a simmer.
179	57	2	Remove the pan from the heat and let stand until the prunes soften, about 25 minutes.
180	57	3	Pour the prunes and port into a large, shallow dish.
181	57	4	Add the garlic, lemon juice and zest and a large pinch each of salt and pepper.
182	57	5	Add the pork roast and turn to coat.
183	57	6	Let marinate at room temperature for 4 hours, turning the meat often.
184	57	7	Preheat the oven to 40
185	57	8	Remove the prunes from the marinade. Strain the marinade into a small saucepan and reserve.
186	57	9	Roll up the anchovy fillets and stuff each one into a prune. Make a deep lengthwise slit in the pork loin, leaving about 1 inch of meat attached. Open the roast like a book and season with salt and pepper. Arrange the stuffed prunes in a row along the slit; close the roast and tie it at 2-inch intervals with kitchen string. Season the roast all over with salt and pepper.
187	57	10	In a large skillet, heat the olive oil until shimmering.
188	57	11	Add the roast, fat side down, and brown it over moderate heat on 4 sides, about 1 minute per side. Set the roast in a roasting pan, fat side up. Roast for about 55 minutes; if the pan juices begin to look very dark, add 2 tablespoons of water to the pan. The roast is done when an instant-read thermometer inserted in the center of the meat registers 14
189	57	12	Transfer the roast to a carving board, cover loosely with foil and let rest for 10 minutes.
190	57	13	Scrape out any blackened bits in the roasting pan. Set the pan over moderately low heat and stir in the flour to make a smooth paste. Slowly whisk in the reserved marinade and simmer, whisking, until the sauce is smooth and thickened, about 3 minutes.
191	57	14	Pour the sauce into a clean saucepan and season with salt and pepper.
192	57	15	Untie the roast and slice it 1/2 inch thick.
193	57	16	Pour any juices into the sauce and reheat before serving it with a pork roast.
194	60	1	Light a grill. Bring a medium pot of water fitted with a steamer insert to a boil.
195	60	2	Cut the heads of broccoli lengthwise into quarters, leaving the florets attached to the long stem. Peel the stems. Steam the broccoli until bright green, about 5 minutes.
196	60	3	Transfer the broccoli to a large bowl and toss with 2 tablespoons of the olive oil. Season with salt and pepper.
197	60	4	In a blender or a mini processor, combine the anchovies, lemon juice and rosemary and puree until smooth. With the blender on, slowly pour in the remaining 1/2 cup of olive oil. Season the anchovy sauce with salt and pepper.
198	60	5	Grill the broccoli over high heat, turning, until lightly charred all over, about 5 minutes.
199	60	6	Transfer the broccoli to a platter and drizzle with some of the dressing.
200	60	7	Serve the remaining dressing on the side.
201	62	1	Combine all the dressing ingredients in a blender and blend until smooth and creamy.
202	62	2	Add a little more water to make it thinner, if desired. Taste for salt and pepper, but be conservative with the salt since the cheese is salty.
203	62	3	Place the lettuce in a serving bowl or on a platter and sprinkle with grated cheese and croutons. Depending on the size of your head of lettuce, you may have more dressing than you need, so just toss lettuce with enough dressing to coat lightly. Or toss salad with dressing and garnish with shaved cheese.
204	64	1	Heat the olive oil In a large skillet.
205	64	2	Add the scallions and garlic and cook over moderate heat until softened, about 3 minutes.
206	64	3	Add the anchovies and cook, mashing them with a fork, for 2 minutes.
207	64	4	Add the olives and stir for 1 minute to heat through.
208	64	5	Add the shrimp and cook, turning once or twice, until they start to curl, about 2 minutes.
209	64	6	Add the wine and simmer, stirring, until the shrimp are just cooked, about 1 minute longer.
210	64	7	Remove the skillet from the heat. Stir in the butter and lemon juice and season with salt and pepper.
211	64	8	Transfer the shrimp to plates and serve.
212	66	1	Fill a bowl with ice water and salt. Bring a saucepan of water to a boil and lower in eggs with a spoon; cook 6 1/2 minutes for a softly set egg.
213	66	2	Transfer eggs to salted ice water (salt helps the shells come off more easily) and cool completely, about 5 minutes. Peel eggs and set aside.
214	66	3	Preheat broiler with a rack set 4 in. from heat.
215	66	4	Brush baguette with oil and sprinkle with salt and pepper to taste. Toast bread, turning once, until warm and golden brown, about 5 minutes. Rub cut side of bread with whole lemon to extract oils from peel.
216	66	5	Use a 1 1/2-in. round cutter to cut 4 evenly spaced holes in each baguette half, or use a knife and scoop out with a spoon. Slice bread crosswise between holes into 8 pieces.
217	66	6	Cut eggs in half crosswise and set an egg into each hole.
218	66	7	Sprinkle eggs with salt and pepper.
219	66	8	Lay 2 anchovies over each and sprinkle with parsley and chives.
220	66	9	*Find in well-stocked grocery stores or Italian markets, or substitute good-quality regular canned or jarred anchovies that you've tossed in a little sherry vinaigrette.
221	67	1	In a small bowl, using a spoon, mash the anchovies and garlic to a paste.
222	67	2	Whisk in the vinegar, followed by the mayonnaise. Gradually whisk in the olive oil and transfer to a small bowl.
223	67	3	Arrange the cucumbers on a work surface. Top each with a cube of feta followed by a tomato. Poke a 4-inch skewer or toothpick through each stack and transfer to a platter.
224	67	4	Serve the skewers along with the aioli.
225	68	1	Preheat oven to 45
226	68	2	To prepare breadcrumbs, place bread in a food processor; pulse 10 times or until coarse crumbs measure 1 cup.
227	68	3	Place breadcrumbs in an even layer on a jelly-roll pan; bake at 450 for 4 minutes or until lightly toasted.
228	68	4	Heat 1 tablespoon oil in a large nonstick skillet over medium heat.
229	68	5	Add breadcrumbs and 1 1/2 teaspoons garlic; cook 2 minutes or until breadcrumbs are lightly browned.
230	68	6	Place breadcrumb mixture in a bowl.
231	68	7	Add parsley and 1/4 teaspoon black pepper.
232	68	8	To prepare pasta, cook pasta according to package directions, omitting salt and fat.
233	68	9	Drain.
234	68	10	Heat 1 tablespoon oil in pan over medium heat.
235	68	11	Combine 1 1/2 teaspoons garlic and next 4 ingredients (through anchovies) in a small bowl; mash with a fork.
236	68	12	Add anchovy mixture to pan; cook 1 minute. Stir in broth; cook 1 minute.
237	68	13	Add pasta; toss well.
238	68	14	Add cheese; toss well.
239	68	15	Place on a large serving platter; sprinkle with breadcrumbs.
240	68	16	Serve immediately.
241	71	1	In a shallow bowl, mix the flour with the salt and cayenne. In another shallow bowl, beat the eggs with the water.
242	71	2	Spread the bread crumbs in a third shallow bowl.
243	71	3	Dredge 4 of the tomato slices in the flour and shake off the excess. Dip them in the egg, then coat with the bread crumbs, shaking off the excess. Repeat with the remaining tomato slices.
244	71	4	Heat the olive oil in a large nonstick skillet.
245	71	5	Add half of the breaded green tomato slices and fry them over moderately high heat until crisp and golden brown, about 2 minutes per side.
246	71	6	Drain the tomato slices on paper towels and transfer them to a large platter. Repeat with the remaining tomato slices. Top each fried tomato slice with an anchovy strip and a lemon wedge and serve immediately.
247	75	1	In a small skillet, heat the olive oil until shimmering.
248	75	2	Add the capers and fry over high heat, stirring occasionally, until browned and shriveled, about 4 minutes. Strain the capers and discard the oil.
249	75	3	Cook the spaghetti in a large pot of boiling salted water until al dente. Meanwhile, in a mortar or mini-processor, combine the anchovies, garlic and lemon zest; pound or process to a thick paste.
250	75	4	Transfer to a large bowl and stir in the parsley, extra-virgin olive oil, lemon juice, crushed red pepper and fried capers.
251	75	5	Drain the spaghetti.
252	75	6	Add it to the fried caper mixture, toss to coat and serve.
253	76	1	Preheat the oven to 35
254	76	2	Arrange the pitas on a baking sheet, rough sides up, and spread each round with 1 tablespoon of the butter.
255	76	3	Bake for about 8 minutes, until crisp.
256	76	4	Let cool and break into large pieces.
257	76	5	Meanwhile, in a small bowl, steep the shallot in the vinegar for 5 minutes. Stir in the olive oil, then add the sour cream and garlic and season with salt and pepper.
258	76	6	In a large bowl, toss the endives with the anchovies and toasted pita.
259	76	7	Add the sour cream dressing and toss well. Spoon onto 4 plates and serve.
260	79	1	Preheat all grates of a well-oiled gas or charcoal grill to high.
261	79	2	Combine all of the butter ingredients together and set aside
262	79	3	Carefully remove the pan from the grill.  Using a spoon, scoop the fuzzy choke from each of the halves.
263	79	4	Transfer the cleaned halves to a new sheet pan. Using your hands or a brush, evenly, but lightly, coat both sides of the artichokes with canola oil.
264	79	5	Place the artichokes, cut side down, on the grate and grill until well marked and lightly charred, 2 to 3 minutes.  Flip and repeat on the second side, grilling for 2 to 3 minutes. While still cut side up, place about 1/2 tablespoon of the butter in each of the cavities and allow it to melt. Squeeze lemon juice over the top and sprinkle with parsley and fleur de sel.
265	79	6	Remove the artichokes from grill and arrange on a serving platter.
266	80	1	Cut each head of radicchio in half lengthwise, then cut each half into 4 wedges. (Leave the cores intact; they'll help hold the wedges together.) Set aside. In a small bowl, whisk together the vinegar, garlic, salt, pepper, anchovies (if using), and 3 tablespoons of the oil; set aside.
267	80	2	Heat the remaining oil in a large skillet over medium heat.
268	80	3	Add the radicchio in a single layer and cook for 3 minutes. Turn the radicchio, add the vinaigrette and oregano, and cook until the radicchio is tender and slightly browned, about 3 minutes more.
269	80	4	Serve warm or at room temperature.
270	86	1	Cook the linguine according to the package directions. Meanwhile, heat the oil in a large skillet over medium heat. Season the shrimp with the pepper and cook until they begin to turn pink, about 2 minutes. Turn the shrimp, add the capers, olives, and anchovies (if using), and cook for 2 minutes more.
271	86	2	Add the marinara sauce and cook until heated through, about 4 minutes. Divide the drained pasta among individual bowls and spoon the shrimp and puttanesca sauce over the top.
282	88	1	In a large bowl, mix the anchovies, mint, chives and 2 tablespoons of the oil.
283	88	2	In a large skillet, heat the remaining 1/4 cup of oil until shimmering.
284	88	3	Add the garlic and crushed red pepper; cook over moderate heat until the garlic is lightly golden, about 3 minutes.
285	88	4	Add the zucchini, season with salt and cook over moderately high heat, tossing, until crisp-tender, about 5 minutes.
286	88	5	Meanwhile, cook the pappardelle in a large pot of boiling salted water until al dente.
287	88	6	Drain, reserving 1/2 cup of the pasta water. Return the pasta to the pot.
288	88	7	Add the zucchini and the reserved pasta water and toss over moderate heat.
289	88	8	Transfer the pasta to the bowl with the anchovies and herbs, season with salt and toss well.
290	88	9	Serve right away, passing the Parmesan and lemon wedges at the table.
291	89	1	Bring 6 quarts water to boil and add 2 tablespoons salt.
292	89	2	Place the noodles in boiling water, and allow 8 to 9 minutes to cook. In a 12 to 14-inch saute pan, place the oil, anchovies, and onion over medium heat and cook. Stir often to break up the anchovies until a paste is formed, about 8 to 10 minutes.
293	89	3	Drain the pasta and toss into the pan.
294	89	4	Add the parsley, toss over high heat 1 minute and place on a plate.
295	89	5	Serve immediately.
296	89	6	To make the dough: Make a mound of the flour in the center of a large wooden cutting board. Make a well in the middle of the flour and add the eggs and milk mixture. Using a fork, beat together the eggs and milk mixture and begin to incorporate the flour starting with the inner rim of the well.
297	89	7	As you expand the well, keep pushing the flour up to retain the well shape. Do not worry that this initial phase looks messy. The dough will come together when half of the flour is incorporated.
445	632629	5	Bake for 45 minute to 1 hour, until the filling is hot and bubbly and the topping is mostly golden brown.Allow to cool for at least 30 minutes before serving.
446	632629	6	Serve warm or at room temperature, topped with ice cream or fresh whipped cream.
450	634854	4	Mix well, add butter and crumble together with a fork.
451	634854	5	Add the oatmeal topping to the mixed berries.
452	634854	6	Place in oven and bake for 30 minutes, until the top is light golden brown.
453	634854	7	NOTE: If you dont have almond meal, just grind some almonds in the food processor until crumbly. Dont process to long to youll have peanut butter!  Worse case scenario use whole wheat flour.
454	634854	8	Calories per serving:  165,  Fat:  6.2,  Cholesterol:  0,  Sodium:  32,  Potassium:  35,  Carbs:  24,  Fiber:  6.5,   Sugar:  10,  Protein: 4
455	715631	1	Juice and zest lemons, set aside.In a small bowl add eggs and salt.
456	715631	2	Whisk until eggs are thinned.
457	715631	3	Transfer eggs to a medium sauce pan.
298	89	8	Start kneading the dough with both hands, using the palms of your hands. Once you have a cohesive mass, remove the dough from the board and scrape up any leftover crusty bits. Discard these bits. Lightly flour the board and continue kneading for 3 more minutes. The dough should be elastic and a little sticky. Continue to knead for another 3 minutes, remembering to dust your board when necessary. Wrap the dough in plastic and allow to rest for 30 minutes at room temperature.
299	89	9	To shape the Bigoli: Knead dough until smooth and tight, and let rest 20 minutes. Note: Do not skip the kneading or resting portion of this recipe. They are essential for a light pasta.
300	89	10	Cut the dough into 6 pieces, and run each piece through a meat grinder set to the smallest extrusion size. As the pasta exits, cut it into 12-inch pieces and immediately dust with flour.
301	89	11	Lay out onto a cookie sheet dusted with cornmeal, being careful to keep the strands separate. Finish all 6 pieces the same way.
302	92	1	Watch how to make this recipe.
303	92	2	Preheat the oven to 300 degrees F.
304	92	3	Put about 3 cups stale Italian bread on a baking sheet and put in hot oven.
305	92	4	Bake for 10 minutes, cool and add to the bowl of a food processor fitted with a bottom blade. Pulse into crumbs.
306	92	5	Bring a large pot of water to a boil over medium heat. Salt the water and add the pasta. Cook until al dente.
307	92	6	Remove 1 cup of the cooking water and reserve.
308	92	7	Drain the pasta and set aside.
309	92	8	In a large saute pan, add 4 tablespoons of the olive oil and the bread crumbs and cook over medium-high heat until golden and well coated.
310	92	9	Remove from the pan to a plate.
311	92	10	Add the remaining 4 tablespoons of the oil to the pan and when hot, add the anchovies and the minced red bell peppers and cook, rapidly, stirring them around with a wooden spoon, for about 2 minutes.
312	92	11	Add the onions and cook for 6 to 8 minutes, stirring frequently.
313	92	12	Add the garlic and chili flakes, cook for an additional 3 to 4 minutes.
314	92	13	Add 1/2 to 1 cup of the bread crumbs and half of the cheese. Stir in the pasta, toss to combine, adding the cooking liquid as needed.
315	92	14	Transfer to a serving platter and garnish with remaining cheese, bread crumbs and parsley.
316	92	15	Serve immediately.
317	96	1	Roast the peppers directly over a gas flame or under the broiler until charred all over; transfer to a rimmed baking sheet and let cool. Discard the skin, stems and seeds; cut the peppers into 1-inch-wide strips.
318	96	2	In a bowl, stir the olives, anchovies, capers, rosemary, vinegar and the 2 tablespoons of olive oil. Fold in the roasted-pepper strips.
319	96	3	Light a grill. Grill the bread over high heat until lightly charred and crisp, 30 seconds per side. Lightly rub each bread slice with the garlic clove and drizzle with olive oil.
320	96	4	Arrange the goat cheese rounds on a large plate and pile the grilled bread alongside.
321	96	5	Serve with the anchovy-and-pepper salad.
322	97	1	Bring a large pot of salted water to a boil.
323	97	2	Add the penne and cook until just shy of al dente, about 7 minutes if the package says 1
324	97	3	Drain.Meanwhile, in heavy 5-quart pot, heat the olive oil over medium heat.
325	97	4	Add the anchovy fillets and cook, stirring, until they dissolve. Be careful for splattering.
326	97	5	Add the minced garlic and cook for just a moment, until aromatic.
327	97	6	Add the flour all at once and cook, whisking frequently, for 90 seconds.
328	97	7	Add the milk, raise the heat to high, and bring to a boil, stirring frequently. When the milk boils, immediately lower the heat to medium-low and simmer until slightly thickened, about 5 minutes.Off the heat, add the mozzarella, fontal, manchego, and 3/4 cup of the Parmigiano. Stir until cheese is melted. Stir in the the basil, parsley, and nutmeg. Season generously to taste with salt and pepper, then stir in the pasta.Preheat oven to 375 F/190 C with a rack in the center.
329	97	8	Pour mixture into a 913-inch baking dish.
330	97	9	Sprinkle with remaining Parmigiano.
331	97	10	Bake until lightly browned and bubbly, about 20 minutes.
332	633338	1	Place the tenderloins on a large dish and wrap a slice of room temperature bacon around each filet, gently stretching the bacon if needed. Secure the ends of the bacon with a toothpick.
333	633338	2	Cut the garlic cloves in half and rub both sides of each filet with the cut ends of the garlic. Season well with salt and pepper on both sides.
334	633338	3	Pre-heat grill to very hot. With tongs, place each steak on the grill and for medium-rare cook for 3-4 minutes, rotating the steaks halfway through 90 degrees for nice grill marks.
335	633338	4	Turn the steaks over and cook another 3-4 minutes.
336	633338	5	Remove from the grill and let rest loosely covered for 5 minutes before removing toothpicks and serving.
337	633338	6	Serve as is or with sauted garlic mushrooms
338	716342	1	Heat the oven to 500 F.Wash and season the chicken with the Suya spice, chilli powder, seasoning cubes, salt and drizzle the oil over it.
339	716342	2	Place the chicken in the oven and grill for 40 minutes. Check the chicken occasionally and flip on both sides so it can cook properly.
340	716342	3	Serve hot garnished with the onions and tomato and a bit of suya spice sprinkled over the chicken.
341	645694	1	Thaw fillets in refrigerator over night. Soak fillets in salt water and ice at for at least 20 minutes - repeat this step at least twice.Wrap edge of fillets with slice of bacon, use toothpicks to hold in position.
342	645694	2	Place fillets in container with enough dressing to completely cover them, add garlic powder and black pepper to taste and allow to marinade for 24 hours.Cook fillets to desired level (medium is very good).
343	645694	3	Remove toothpicks!
444	632629	4	Layer this crumbly mixture on top of the apple-walnut filling. Make sure the entire dish is covered in an even layer of sugary goodness.Use the remaining 3 tbsp. of cold, cubed butter to dot the top of the dish. This will melt and add moisture to the very top during baking.
449	634854	3	In a small bowl, add oatmeal, almond meal, brown sugar and cinnamon.
344	645694	4	Serve with salad, baked potato, sourdough bread, and good Merlot.Comments: There are any number of excellent marinades for duck - Teriyaki sauce with pineapple juice; Dales with a shot of bourbon, and a splash of regular (sugar, caffiene, colorings - the real thing) Coke; sweet and sour sauce; or Bar-b-Que sauce. The key to good grilled duck is cooking on low heat and brushing on the marinade regularly to keep the meat moist.This recipe is REALLY a cop out, but one of the most popular the with people I hunt with. Its great over the grill, camp fire, or cook stove in the duck blind.
345	647524	1	Season roast with salt and pepper, put in roaster with onion and a little water.
346	647524	2	Bake at 325 degrees for 3 hours. Take out and cool.
347	647524	3	Heat soup until creamy, add all pan drippings from roast and add a bit of Master Gravy or Kitchen Bouquet to darken. Slice beef and add to gravy mixture and simmer slowly, approximately 1 hour.
348	665574	1	Mix flour and salt in basin make a hollow in the centure and drop in the egg. Stir with a wooden spoon and add liquid gradually, until all the flour is worked in. Beat well and add remaining liquid. Melt fat in a shallow dripping tin or four small tins.
349	665574	2	Place in oven until haze appears.
350	665574	3	Pour the batter into the large tin, or half fill small tins.
351	665574	4	Bake in hot oven (425/F to 450/F, Gas 7 to
352	665574	5	for about half an hour for a large pudding, 20 minutes for the small puddings.
353	665574	6	To make a deferent pudding you could add choped onions to the batter or mixed hurbs are good.
354	649722	1	Combine lemon juice, salt and dill weed. Trim all visible fat and place beef chuck steak in plastic bag or dish; add marinade, turning to coat. Tie bag securely or cover dish and marinade in refrigerator 6 to 8 hours or overnight, turning at least once.
355	649722	2	Remove steak from marinade, press pepper into surface of both side of meat.
356	649722	3	Place steak on broiler pan and broil 10 to 12 minutes on each side. Carve steak into thin slices.
357	654485	1	Preheat oven to 350 degrees f. Spray a mini-muffin tin lightly with cooking spray. Toss the add-ins with a small spoonful of dry pancake mix or flour, to keep them from sinking to the bottom of the muffin tins.Spoon batter into each muffin cup about 1/2 full.
358	654485	2	Sprinkle with a little of the add-in of your choice (or you can just make them plain, of course). Top with a bit more batter, filling the muffin tins about 3/4 of the way full.
359	654485	3	Bake for about 12 minutes, until cooked through.
360	654485	4	Remove from the muffin tins and brush lightly with butter. Repeat with remaining batter.
361	654485	5	Serve warm with maple syrup.
362	662744	1	Brown and drain ground beef.
363	662744	2	Season according to taco seasoning instructions.
364	662744	3	Turn off heat, and mix in shredded cheese with taco meat.
365	662744	4	Fill egg roll wrappers.
366	662744	5	Brush egg rolls with olive oil.
367	662744	6	Bake at 375 for 15 minutes, flipping egg rolls at 8 minutes.
368	662744	7	Serve hot with sour cream!
369	662744	8	Experiment with these things!
370	662744	9	Add peppers, rice, or refried beans. Make them your own.
371	643829	1	Cook in pan for 3-4 minutes.
372	643829	2	Ketchup
373	643829	3	Sugar
374	643829	4	Garlic powder
375	643829	5	Salt
376	643829	6	Some water
377	645879	1	Wipe dry the chicken.Season with salt and pepper.
378	645879	2	Mix marinade together and rub onto chicken.Preheat grill and when hot, place chicken under it.If you do not have a grill, roast it in your oven.Cook till golden brown, turning chicken over once and basting it with marinade occasionally.
379	634698	1	For 4 people
380	634698	2	Heat grid well.
381	634698	3	Place beef on grid and grill on all sides. When the surface turns light brown, dip in ice water for a few seconds. Dry with a cloth, wrap in Saran Wrap and place in the refrigerator.Prepare condiments.
382	634698	4	Cut lemon into 8 wedges. Pare daikon in paper thin sheets, cutting with bottom part of knife while rotating the daikon.
383	634698	5	Roll daikon sheet and slice thinly crosswise, thus making very thin and long strips. Do the same with cucumber.
384	634698	6	Cut beef into thin slices.
385	634698	7	Place daikon strip, cucumber and beef slices in a serving dish. Put other condiments on the side.
386	634698	8	Place scallions on beef.
387	634698	9	Pour soy sauce into small individual serving dishes and add condiments to taste. The beef is dipped lightly in the soy sauce.
388	659285	1	Preheat oven to 190 degree Celsius.
389	659285	2	Combine the ingredients into a mixing bowl
390	659285	3	Stir and mix well in one direction and form into ball shape.
391	659285	4	Spray the oven tray/pan with non-stick spray.
392	659285	5	Place the meat balls on the greased oven pan.
393	659285	6	Bake for 20 minutes; try to shake the pan once a while to ensure the balls cook at all sides.
394	659285	7	Bake until golden brown or the inside of the meat should not be pink.
395	659285	8	Serve the satay meat ball with chili sauce or sweet chili dipping sauce.Tips:You can use pork or chicken mince for this recipe too.
396	716300	1	Dissolve the yeast in warm water and leave to stand for about 5 minutes.
397	716300	2	Mix the oil, flour, salt, sugar and mashed plantain and pour in the dissolved yeast.Knead the dough till its elastic which may take aBout 15-20 minutes By hand or 10 minutes in a mixer.Coat a Bowl lightly with oil and place the dough in it. Cover with a plastic wrap and leave to rise between 1.5 – 2 hours.While the dough is rising, heat up the oil for the sauce, fry the Blended tomato and pepper, season and stir fry the Beef in the tomato sauce. Set aside.When the dough rises, divide into two.
398	716300	3	Sprinkle some flour on a flat surface and with a rolling pin, flatten out the dough but not excessively.
399	716300	4	Cut the dough into your desired shape, rub some oil on it and spread your sauce and toppings on it and set aside.
400	716300	5	Heat up your oven to 350 F and place your pizza dough on a lightly oiled foil pan and
401	716300	6	Bake for 12-15 mins.
402	716300	7	Serve warm
403	649024	1	(The Meades)
404	649024	2	Mix it all together and marinate at least 2 hours. Can either cook it on the grill as kebabs or stir-fry by itself. Enjoy.When I don't have sirloin tips, I use flank steak and it tastes just as good. Also, I substitute hot pepper sesame oil and also add cayenne pepper for more kick. The sugar allows the beef to caramelize a little (I tried using cane sugar once but it didn't caramelize).NOTES: Just tried this recipe recently (4 or 5 times) and it is absolutely wonderful - from Omaha Steaks recipe book
405	660133	1	Wash the chicken inside and out and pat dry. Make sure the skin is nice and dry so the skin gets crispy. Season well with salt and pepper inside, out and under the skin.
406	660133	2	Mix the butter with the garlic, chilli and lemon rind. Season a bit with salt and pepper. Stuff the flavoured butter under the skin over the breast, legs and back. Stuff the lemon half into the cavity.
407	660133	3	Pre-heat the oven to 400F. Toss the two kinds of potatoes in the bottom the the baking pan with the chilli, salt and pepper to taste and a generous helping of olive oil.
408	660133	4	Place a rack over the vegetables. Position the chicken breast side up on the rack.
409	660133	5	Bake for the first 15 minutes at 400F. Then drop the temperature and continue to cook for about an hour at 300F.
410	660133	6	Halfway through cooking turn the chicken on its breast. Spoon over some of the juices.
411	660133	7	Later, to check for doneness, pierce the thickest part of the chicken (the thigh). If the juices run clear the chicken is ready, if not continue cooking.
412	660133	8	Serve chicken on a platter on the bed of roasted potatoes.
413	658136	1	In a saucepan, heat oil over high heat until just smoking and brown beef cubes.
414	658136	2	Add minced ginger and scallions and stir fry until aromatic, about 30 seconds.
415	658136	3	Add sherry, soy sauce, star anise, sugar, and 1 cup of water.Bring to a boil, reduce heat to low, and simmer until meat is tender when pricked with a fork, 45 minutes to 1 hour. There should be about one-third of cooking juices left. If there is more, remove meat and boil liquid over high heat to reduce.
416	658136	4	Serve meat in juices.This dish improves if prepared ahead of time and reheated. It also freezes beautifully.1, 9
417	645710	1	In a small bowl, combine all of the ingredients for the aioli, season to taste with salt.Preheat a grill pan (a nonstick skillet can be used as well) over med-high heat until very hot.
418	645710	2	Brush the cut-sides of the buns with melted butter.
419	645710	3	Drizzle a little bit of oil into the pan and using a wad of paper towel, carefully wipe out the excess (you are just reinforcing your nonstick surface). Toast the buttered sides of the buns, then set aside while cooking the fish.Pat the fish dry and season with salt & pepper (or seasoning of your choice).
420	645710	4	Drizzle a little bit of oil over the fish and rub it over the entire surface of the fish to evenly coat with oil.
421	645710	5	Add the fish to the hot pan and cook, turning once, until the fish is cooked through (cooking time will vary based on the thickness of your fish, somewhere between 2-4 minutes per side).erve the fish on the toasted buns, slathered with the aioli and toppings of choice.
422	664643	1	In a large covered saucepan, bring the water and salt to a boil over medium heat.
423	664643	2	Add the bulghur and carrots, remove from the heat, cover and let stand until the bulghur has softened and absorbed all the liquid, about 15 minutes.
424	664643	3	Drain well.
425	664643	4	In a large bowl, mash the tofu. Stir in the bulghur mixture, egg white, mint, scallions and cayenne, stirring well. Stir in the bread crumbs, 1/4 cup of the flour, the ketchup and mustard.
426	664643	5	Preheat the oven to 400F. Form the bulghur mixture into 4 patties about 1 inch thick and 4 inches in diameter. Dredge the patties in the remaining flour.
427	664643	6	In a large nonstick skillet, warm the oil over medium heat until hot but not smoking.
428	664643	7	Add the patties to the skillet and saute until crusty, about 4 minutes per side.
429	664643	8	Transfer to a nonstick baking sheet and bake for about 5 minutes, or until heated through.
430	664643	9	Serve the burgers on the hamburger buns with the lettuce, tomato and alfalfa sprouts.
431	664643	10	NOTES : The beef hamburger is appreciated for many reasonsits nutritional attributes, however, not being among them. Vegetarian "burgers," on the other hand, rarely have the meatiness many people crave. This meat-loaf-style burger seasoned with mint and scallions manages to bridge the gap.
432	631814	1	Combine the chuck, basil, sun-dried tomatoes, onion, garlic, and salt in a large bowl, handling as little as possible. Shape into 2 patties to fit the bun size. Loosely cover with plastic wrap and set aside.For the fennel:Grate 1/2 teaspoons zest from the lemons.
433	631814	2	Put the fennel rings in a medium-sized bowl (I used half a fennel bulb) and juice the lemon over half the fennel and toss to coat all the fennel rings.
434	631814	3	Add oil and season with salt.
435	631814	4	Put the fennel in a grill basket and grill, shaking the basket occasionally, until soft, 10 to 12 minutes. (I did this on the stove top)
436	631814	5	Transfer the fennel to a sheet of foil, sprinkle with the lemon zest, and wrap to keep warm.
437	631814	6	Heat a large, heavy nonstick fire-proof skillet on the grill.
438	631814	7	Add the bacon and cook until crisp.
439	715574	1	Add the strawberries, whole milk and vanilla ice cream to a blender, and blend until smooth.
440	715574	2	Pour into cold glasses that have been kept in the freezer.Return the shakes to the freezer for about 5 minutes, or until they are thick.Top with whipped cream and sliced strawberries.
441	632629	1	Preheat oven to 350-degrees F.Use the 1 tsp. butter to grease the sides and bottom of an oven-proof baking dish.*In a large, deep bowl, combine the apples, sugar, lemon juice, cinnamon, nutmeg and walnuts.Toss to insure all apples are well coated with the mixture.
442	632629	2	Pour into the prepared baking dish.In another deep bowl, mix the other sugars, flour, oatmeal, salt and cinnamon until it is well blended.
443	632629	3	Add the 1/2 lb. of cold butter, a little at a time, and use a pastry cutter or large fork to mash into a rough topping.The butter should be very cold so it does not melt during this mashing process; it should remain in small beads or chunks, about the size of peas.When all this butter has been incorporated, add the water and mix again, to further create a crumb-like topping (much like that found on a crumb-topped pie or coffee cake).
447	634854	1	Preheat oven to 350
448	634854	2	In a baking dish add berries and maple syrup, give a light stir, set a side.
458	715631	4	Add sugar, lemon juice, and zest. Turn heat on to medium and stir with plastic whisk or spoon. (Do not use metal)
459	715631	5	Add softened butter to pan. Stir constantly for 4-6 minutes or until curd has thickened.
460	715631	6	Remove from heat and transfer to glass jar or container with lid. Chill for 1 hour.
461	633660	1	Preheat oven to 180C/350F.
462	633660	2	Roll pastry out to a thickness of about 3 mm (a little more than 1/10 in) and line flan tin with pastry. Prick pastry gently with a fork. Press a sheet of foil out over pastry and into the corners.
463	633660	3	Bake in a preheated oven for about 15 minutes.
464	633660	4	Remove foil and continue cooking until pastry is light brown in color.Meanwhile, in a bowl mix eggs, sugar, grated lemon rind and cream.
465	633660	5	Mix in lemon and orange juice.
466	633660	6	Pour preparation into the baked pastry shell and bake in a preheated oven for about 12 to 15 minutes until the centre of the custard appears to have just set. Allow tart to cool before carefully unmoulding.A short while before serving, peel the extra lemon, using a small sharp knife, removing all the white skin as well.
467	633660	7	Cut lemon into thin slices about 2 mm thick. Arrange lemon slices over tart in a circular pattern and sprinkle the top generously with icing sugar.
468	633660	8	Place under a hot grill for 1 to 2 minutes to melt the icing sugar and give the top of the tart a lovely glaze.
469	633660	9	Cut into slices and
470	649230	1	Melt butter in a sauce pan, add salt, cinnamon, sugar and nutmeg and stir until smooth.
471	649230	2	Add remaining ingredients, cover and cook over low heat 15 minutes, stirring occasionally.
472	649230	3	Brush or marinate lamb ribs in sauce before grilling.Rub lamb riblets with salt and pepper and thread on barbecue spit or place in crown on grill. Cook, 5 to 6 inches above coals for about 45 minutes or until well done.
473	649230	4	Brush with sauce every 15 minutes.
474	649230	5	Serve riblets with remaining sauce.
475	632117	1	Cream the butter, add egg well beaten, almonds, sugar, brandy, and spices mixed and sifted with flour.
476	632117	2	Roll mixture to one-fourth inch in thickness, shape with a round cutter first dipped in flour, and bake in a slow oven.
477	663175	1	Spray a foil-lined baking sheet with nonstick spray.
478	663175	2	Place fish on baking sheet.Mince green onions, basil, ginger, and garlic.Rub mixture on both sides of the fish.Season with salt, pepper, and cayenne.
479	663175	3	Brush with sesame oil.
480	663175	4	Let stand at room temperature for 20 minutes, or cover and refrigerate for up to 2 hours.Preheat oven to 450F.
481	663175	5	Bake fish uncovered for 10-12 minutes, until golden.
482	633324	1	Preheat oven to 350-degrees.
483	633324	2	Arrange bacon slices on baking sheet.
484	633324	3	Bake until pale golden, about 8 minutes.
485	633324	4	Cut each slice crosswise in half. Cool.
486	633324	5	Wrap 1 bacon piece around sides of each scallop and secure with a toothpick.
487	633324	6	Preheat oven to 400-degrees.
488	633324	7	Place scallops on baking sheet and bake until cooked through, about 10 minutes.
489	633324	8	Meanwhile, boil cream in heavy large skillet until reduced to 3/4 c., about 3 minutes.
490	633324	9	Add mustard and syrup and boil until thickened to sauce consistency, about 3 minutes. Season to taste with salt and pepper.
491	633324	10	Remove toothpicks from scallops. Spoon sauce evenly onto 4 small plates.
492	633324	11	Arrange scallops decoratively atop sauce.
493	633324	12	Sprinkle with chives and serve.
494	644357	1	Heat the oil on a high heat and add the shallots, allow them to cook for about 30 seconds.
495	644357	2	Add the garlic and cook for a further 30 seconds.
496	644357	3	Add the prawns, cook for about one minute on each side.  They are cooked when they turn from black/grey to pink.  To make sure they are cooked through, you can either eat one (my preferred way to check!) or check the thickest part, the back area to make sure the pink colour goes all the way through.
497	644357	4	Squeeze the lemon juice into the pan to deglaze, mix through.
498	644357	5	Add the parsley, salt and pepper.  Check for seasoning and serve straight away.
499	644357	6	Tips and Variations
500	644357	7	You can add some fresh chili or some dried chili flakes if you want a bit of spice.
501	644357	8	Serve with pasta (I like spaghetti, spaghettini, linguini or fettuccine  as long as its a good quality pasta)
502	644357	9	Goes well with rice too.
503	661570	1	Add 2-3 inches of water to the bottom of a steamer and bring to a boil.  Meanwhile, place halibut steaks on a plate that fits inside the steamer.  Lightly salt and pepper steaks.
504	661570	2	Combine soy sauce, sesame oil and pepper in a small bowl.  Spoon sauce over halibut steaks.  Get every last bit.  Top with ginger and 1/2 of the scallions.  Steam for 8-10 minutes, depending on thickness of halibut steak.  Check water level occasionally during cooking to ensure steaming water does not evaporate fully.
505	661570	3	Add more boiling water if needed.
506	661570	4	Remove from steamer and top with reserved scallions and cilantro.
507	661570	5	Serve immediately with rice and a side of stir fried vegetables.
508	645824	1	Mix the garlic and onion with the vegetable oil.
509	645824	2	Add the prawns and toss.Marinate in the refrigerator (at least 3 hrs).Grill the prawns on a barbecue or griddle for about 5 minutes, turning once.
510	645824	3	Mix together the salt, pepper and the juice from the lime to make a dip for the prawns.
511	652061	1	Get your salted water going and once it starts to boil add the pasta.  Cook according to the instructions on the box.Put pan on medium-high heat and add oil.  Once its hot enough at the diced onion and saute till soft.  Then add garlic.
512	652061	2	Add mushroom when you start to smell the garlic and give everything a good stir.
513	652061	3	Add the miso paste into the mushroom and onion mix.  Stir it around then pour in the heavy cream.  Stir until all of the miso paste have dissolved into the cream.By now you should have a nice light brown bubbly creamy mixture.  Give it a taste now.  Season accordingly.  Now add the pasta into the cream. If it is a bit dry add some pasta water into it.
514	652061	4	Serve it up on a nice plate and sprinkle the shiso leaves on top and dig in.
515	654886	1	Strain the diced tomatoes.In a large bowl, add the remaining diced and chopped vegetables, as well as the oil and vinegar.Season to taste with salt and pepper, and refrigerate until well chilled.Once sauce is sufficiently chilled, start to cook pasta in well-salted water.Strain the pasta, then place it in a serving dish.
516	654886	2	Drizzle with olive oil and toss until well coated.Spoon the chilled sauce on the top, and serve immediately.
517	655806	1	In a food processor, blend parsley, garlic, nuts and oil until smooth.
518	655806	2	Mix in yogurt and cheese.  Season with salt and pepper.Cook pasta in a large pot of boiling water, stirring occasionally until al dente.Toss pasta and pesto sauce together in a large bowl.
519	649034	1	Season the beef with salt and pepper. In a mixing bowl, combine the oil, soy sauce, garlic and ginger. Season with crushed red pepper to taste.
520	649034	2	Place the meat in a shallow bowl.
521	649034	3	Pour the marinade over the meat. Cover and refrigerate for at least 1 hour or overnight.
522	649034	4	Remove and bring to room temperature. Preheat the hibachi.
523	649034	5	Remove the meat from the pan, reserving the marinade.
524	649034	6	Place the marinade in a saucepan, over medium heat. Bring to a boil and cook for 6 to 8 minutes or until the mixture reduces by 3/
525	649034	7	Remove, set aside, and keep warm. Grill the meat for a couple of minutes on each side, for medium rare. To serve, spoon the rice in the center of each plate.
526	649034	8	Lay the strips of meat around the rice.
527	649034	9	Drizzle the sauce over the
528	634404	1	Melt butter and olive oil in large skillet; add garlic and shallots.  Saut for a moment; add rice.  Stir to combine.
529	634404	2	Add heated chicken stock,  -  cup at a time.  Stir after each addition, and cook until liquid is completely evaporated before adding more liquid.
530	634404	3	When adding the last of the chicken stock, add the parsley and the cheese.  Cook until liquid is completely evaporated.
531	632797	1	Mix soy sauce, cornstarch, sugar, and ginger. Coat meat with soy sauce mixture.
532	632797	2	Heat 1 tablespoon oil in a large frypan.
533	632797	3	Add green pepper strips. Cook for 2 minutes, stirring constantly.
534	632797	4	Remove green pepper from pan.
535	632797	5	Heat remaining 2 tablespoons oil.
536	632797	6	Add meat. Cook for 1 to 2 minutes, stirring constantly, until beef is lightly browned.
537	632797	7	Add green pepper and pineapple.
538	632797	8	Heat through.
539	632797	9	Serve over rice.NOTE: Steak is easier to cut when partially frozen.
540	641559	1	Marinate beef and tofu overnight in Korean barbecue marinade.Cook rice and keep warm.In sesame oil and a pinch of salt, saut carrots and zucchini until almost tender. If necessary add a bit more sesame oil and toss in the remaining vegetables, garlic and a pinch of sugar and continue to saut approximately 2 minutes, or until the vegetables are almost done (they will continue to cook in the dolsot or stone bowl)Broil or barbecue the beef.
541	641559	2	Pour a 1/2 - 1 teaspoon of sesame oil in the base of each stone bowl. Divide rice between the 4 stone bowls. Arrange all ingredients on top of the rice side by side around the bowl. Put a teaspoon (or more depending on taste) of the Korean chilli paste on top of the vegetables and in the middle of the bowl place an egg yolk.
542	641559	3	Pour a tablespoon of sesame seed oil around the edge of the bowl.
543	641559	4	Place stone bowl on top of stove and on high heat leave for approx 5 minutes or until you can hear the rice popping and crackling.
544	641559	5	Remove from heat and serve. Be very careful as the stone bowl will be extremely hot.
545	642125	1	Crack the eggs into the leftover rice. Season with some salt and pepper.Use a fork and mix the rice and eggs around until well combine.
546	642125	2	Heat some oil in a pan. Over the low flame, snip the kaffir leaves into the oil. When the leaves appear to be crispy, spoon them out from the oil and spread them out and rest on a kitchen towel.
547	642125	3	Add in the rice-egg mixture into the same pan over medium flame. Use a spatula and check if the side (facing the pan) is looking like an omelette texture (golden brown).
548	642125	4	When the omelette texture is achieved, flip the mixture to cook the other side. As it cooks, start breaking the mixture with a spatula to resemble loose rice grains.
549	642125	5	Add in the red curry paste and mixed vegetables and stir to combine. The fried is ready when the mixed vegetable is heated through.
550	642125	6	Sprinkle crispy kaffir leaves over fried rice before serving.
551	664975	1	In a small saucepan over medium-high heat, stir together mirin, vinegar, soy sauce, honey, ginger and wasabi to taste. (
552	664975	2	Add the wasabi incrementally, tasting as you go.)Bring to a boil. Reduce the heat to medium and cook, stirring occasionally, until glaze thickens slightly, about 5-10 minutes.
553	664975	3	Remove from the heat.Preheat oven to 425F.Lightly coat an oven-proof skillet with olive oil and heat on medium-high.Season the salmon with a little kosher salt &amp; fresh cracked pepper.When the oil is hot and begins to shimmer, add the salmon, skin side up.Sear, without moving it around for 3-4 minutes.  Turn the salmon over, skin side down.
554	664975	4	Brush some of the glaze onto the salmon and then place the skillet of salmon into the oven for about 4 minutes.Spoon the remainder of the sauce over the salmon and serve hot.
555	654435	1	In a bowl combine 1 tbsp olive oil, salt, pepper, garlic, lemon juice, and dill.
556	654435	2	Add salmon fillets.
557	654435	3	Let them marinate for 15 minutes at room temperature.Preheat a large skillet on medium heat for 2 minutes.
558	654435	4	Add 1 tsp olive oil and then add salmon. Cook for 5 minutes per side. Salmon should be done when it flakes easily with a fork.
559	654435	5	Transfer to plates.
560	654435	6	Serve with lemon wedges.
561	655130	1	Split cake in half to a thickness of about 3cm and cut 1 half into 4 rounds, roughly the size of a peach half.
562	655130	2	Dice half the peaches.
563	655130	3	Place a round of sponge cake in each glass dish and soak with brandy.
564	655130	4	Place a peach half on sponge, hollow side up, and place a scoop of ice cream on each peach.
565	655130	5	Pour raspberry syrup over ice cream, decorate with whipped cream and chopped nuts and scatter round diced peach and extra fresh raspberries.
566	636857	1	First up, you'll beat your eggs white until they are a stiff foam.Now you'll add in your sugar, vanilla, cinnamon, nutmeg, and salt.
567	636857	2	Mix it together and add in your nuts. Coat them well.
568	636857	3	Heat up your oven to 350 degrees.Now drop your butter on a jelly roll pan and pop it in the oven and let it melt down. When it completely melted, bring it out, spread it around the pan and place your nuts on the pan.
569	636857	4	Place your nuts in the oven for 20 minutes, being sure to turn once or twice. Bring them out and cool them completely.
570	646825	1	In a large bowl combine the butter and sugar and mix until smooth.
571	646825	2	Add eggs and vanilla and continue to mix on low.
572	646825	3	Combine the baking powder with the flour and add slowly, while the mixer is on low, to the butter mixture.
573	646825	4	Add the finely chopped walnuts and the package of cherry gelatin to the batter.
574	646825	5	Form the dough into a disc and roll out to a quarter inch thickness. Using cookie cutters form into your favorite holiday shapes.
575	646825	6	Place cookies on parchment paper and bake 10 to 12 minutes or until slightly golden on edges.
577	716344	1	sdf
578	716345	1	dsf
579	716346	1	sdfsf
\.


--
-- Data for Name: new_recipes; Type: TABLE DATA; Schema: public; Owner: atip
--

COPY public.new_recipes (id, name, duration_minute, health_score, serving, image, user_id) FROM stdin;
\.


--
-- Data for Name: recipes; Type: TABLE DATA; Schema: public; Owner: atip
--

COPY public.recipes (id, name, duration_minute, image, calories, serving) FROM stdin;
655130	Peach Melba	45	https://liliebakery.fr/wp-content/uploads/2022/07/Peche-melba-Lilie-Bakery.jpg	300	100
654886	Pasta Verano	45	https://i.blogs.es/00ba3a/ensaladas-pasta-4/450_1000.jpg	500	1
645824	Grilled Prawns	45	https://hips.hearstapps.com/hmg-prod/images/grilledshrimp-1525299887.jpg?crop=0.668xw:1.00xh;0.167xw,0&resize=1200:*	250	4
654485	Pancake Bites	45	https://myfoodstory.com/wp-content/uploads/2017/09/chocolate-stuffed-mini-pancake-bites-6.jpg	300	36
26	Sliced Baguette with Radishes	25	https://assets.bonappetit.com/photos/57afcf95f1c801a1038bd4a3/master/w_646	250	16
661570	Steamed Halibut	45	https://leitesculinaria.com/wp-content/uploads/2020/02/steamed-halibut-fresh-ginger-fp.jpg	350	4
647524	Hot Sliced Beef	45	https://www.fromvalerieskitchen.com/wordpress/wp-content/uploads/2020/12/Deli-Style-Roast-Beef-8.jpg	400	1
25	Anchovy Fries with Aioli	45	https://img.sunset02.com/sites/default/files/image/recipes/su/11/09/SU_Food_0911/anchovy-fries-su-x.jpg#	300	8
12	Roasted Peppers	4500	https://images.unsplash.com/photo-1518133299975-8e1b628e1cfd?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MjB8fFJvYXN0ZWQlMjBQZXBwZXJzJTIwd2l0aCUyMEJvcXVlcm9uZXN8ZW58MHx8MHx8fDA%3D&auto=format&fit=crop&w=900&q=60#	250	12
632117	Almond Cookies	45	https://www.simplyrecipes.com/thmb/CVUmMGlg0DkuW1p1KPLRg4YP1UA=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc()/Simply-Recipes-Chinese-Almond-Cookies-2-LEAD-12-a349ad89121849149f7fee7336e26798.jpg	150	1
652061	Miso Cream Pasta	45	https://i0.wp.com/beyondthenoms.com/wp-content/uploads/2022/01/Miso-Pasta-9.jpg?fit=1365%2C2048&ssl=1	550	1
16	Baguette with Radishes	45	https://images.unsplash.com/photo-1612284640348-a7a5b3158795?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MTB8fEJhZ3VldHRlJTIwV2l0aCUyMFJhZGlzaGVzfGVufDB8fDB8fHww&auto=format&fit=crop&w=900&q=60#	300	1
641559	Dolsot Bibimbap	45	https://sweecooks.com/wp-content/uploads/2021/05/1CEBA3BC-6D0E-4CCF-A5C3-40D604436D68-scaled.jpeg	500	4
663175	Thai-Style Fish	45	https://asianinspirations.com.au/wp-content/uploads/2018/12/R01629_Thai_Deep_Fried_Fish_with_Pineapple_Sweet_Chilli_Sauce.jpg	400	4
57	Pork with Prunes	45	https://blog.williams-sonoma.com/wp-content/uploads/2016/08/sept-14-Pork-Tenderloin-with-Port-Wine-and-Prunes.jpg	450	6
664975	Wasabi & Honey Glazed-Salmon	20	https://i0.wp.com/cookswellwithothers.com/wp-content/uploads/2019/06/IMG_0178.jpg?resize=1140%2C1520&ssl=1&is-pending-load=1	450	2
632629	Apple-Walnut Crisp	45	https://static.onecms.io/wp-content/uploads/sites/19/2000/10/01/apple-crisp-ck-223084-x.jpg	300	4
29	Chicory & Anchovy	120	https://i.pinimg.com/736x/7a/ca/16/7aca164d5d1ff9113db8bcb34a9bc196--skate-east-coast.jpg#	150	4
645879	Grilled Sesame Chicken	45	https://www.ambitiouskitchen.com/wp-content/uploads/2022/08/Grilled-Sesame-Chicken-6.jpg	300	1
658136	Red-Braised Beef	45	https://assets.bonappetit.com/photos/5c4b21e785b9bd2cf3b17454/16:9/w_4800,h_2700,c_limit/red-wine-braised-short-ribs.jpg	550	2
715574	Strawberry Shake	45	https://www.chelseasmessyapron.com/wp-content/uploads/2020/04/Strawberry-Milkshake-1.jpg	300	6
645694	Grilled Duck	45	https://s3.us-east-1.amazonaws.com/assets.mapleleaffarms.com/content/_1200x630_crop_center-center_82_none/Grilled-Duck-Legs.jpg?mtime=1656361324	400	6
633338	Bacon Wrapped Filet Mignon	45	https://amandascookin.com/wp-content/uploads/2022/12/Bacon-Wrapped-Filet-Mignon-RCSQ.jpg	600	4
66	Egg & Anchovy Crostini	35	https://assets.bonappetit.com/photos/57acc7b1f1c801a1038bc76c/1:1/w_2560%2Cc_limit/crostini-with-crushed-eggs-and-salted-anchovies.jpg	150	8
60	Grilled Broccoli with Dressing	30	https://static01.nyt.com/images/2022/11/02/dining/ep-air-fryer-broccoli/merlin_215733819_1e00aa8a-8fb3-4a37-a8a9-30cd5558a635-threeByTwoMediumAt2X.jpg#	180	6
644357	Garlic Shrimp	45	https://therecipecritic.com/wp-content/uploads/2021/08/garlicbuttershrimp.jpg	250	4
646825	Holiday Cookies	45	https://plus.unsplash.com/premium_photo-1669833444242-1fb4940fb5d2?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1770&q=80	200	24
649230	Lamb Riblets	45	https://simply-delicious-food.com/wp-content/uploads/2019/03/sticky-lamb-ribs-4.jpg	500	1
649034	Korean Bulgogi	45	https://thestayathomechef.com/wp-content/uploads/2021/02/Korean-Beef-Bulgogi-4.jpg	400	1
631814	$50,000 Burger	45	https://images.unsplash.com/photo-1568901346375-23c9450c58cd?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1599&q=80	1200	4
76	Crisp Pita Bread Salad	25	https://i0.wp.com/justinesnacks.com/wp-content/uploads/2022/10/brussel-sprout-salad-with-anchovy-dressing.jpg?fit=1638%2C2048&ssl=1#	300	4
46	Orecchiette with Cauliflower, Anchovies & Pistachios	45	https://www.177milkstreet.com/assets/site/Recipes/Pasta-Cauliflower-Lemon-Pistachios.jpg#	450	6
716344	A	1	https://bit.ly/3oAddoE	1	1
42	Grilled Mozzarella Sandwich 	45	https://images.squarespace-cdn.com/content/v1/63ecf329e4e93d3adcd8a4a1/1677544314886-JN8BPT8A1DT8H9OIHBSD/mozzarellatapenadelemonsandwich7.jpg#	450	1
62	Avocado Caesar Salad	45	https://australianavocados.com.au/wp-content/uploads/2022/02/Avocado-Caesar-Salad.png#	220	6
67	Greek Salad Skewers	30	https://www.littlebroken.com/wp-content/uploads/2020/12/Greek-Salad-Skewers-8.jpg	180	36
43	Pressed Summer Sandwich with Eggs & Anchovies	15	https://images.food52.com/EYGIMFHi6DKys0MbznISm0NFFs8=/fit-in/1200x1200/d13f0ee2-8e15-40b4-b580-ec7fd9584d9d--2014-0311_finalist_decadent-fried-egg-sandwich-020.jpg#	400	15
50	Hard-Cooked Eggs with Crumbs	45	https://www.linsfood.com/wp-content/uploads/2018/01/Italian-Salsa-Verde-1-500x500.jpg#	160	20
645710	Grilled Fish Sandwich	45	https://www.sunset.com/wp-content/uploads/fish-sandwiches-60446-0818-1600x800.jpg	400	4
715631	Fresh Lemon Curd	45	https://i2.wp.com/completelydelicious.com/wp-content/uploads/2023/01/how-to-make-lemon-curd-7.jpg	250	2
643829	Fried Wonton	45	data:image/jpeg;base64,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	150	1
30	Greens Salad with Gruyère	40	https://hillstreetgrocer.com/application/files/1516/0247/7764/Grilled_cos_lettuce_and_bacon_salad.jpg#	200	6
37	Roasted Cauliflower with Anchovy Bread Crumbs	60	https://images.squarespace-cdn.com/content/v1/51ffaae6e4b0622dbb490b6d/1515353595189-3ZXLCNXLPB9TZIN3R0A5/IMG_0368.JPG?format=1000w#	350	3
716342	Chicken Suya	45	https://www.fusioncraftiness.com/wp-content/uploads/2019/05/Suya8LRX-720x720.jpg	350	1
633324	Bacon Scallops	45	https://www.thespruceeats.com/thmb/bpnpU7ZoLV_kxl_5HgdetQKJozU=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc()/easy-bacon-wrapped-scallops-3060665-hero-01-2537869202884b1db161ff09637c51f1.jpg	250	4
716346	A	1	https://www.eatingwell.com/thmb/IbDeVkiVaS_m1yk5Fcao8MlOFSI=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc()/EWL-250205-basic-risotto-09-D-e9fc9441a50245909de19f1a05b790f3.jpg	1	1
96	Roasted-Pepper Salad with Cheese	30	https://images.food52.com/uSHRypd2j_uno5FLybLa1ew6VGo=/1200x900/ed552748-1425-42c2-affc-055127d47480--anchovy_peppers5.jpg#	400	6
19	Fennel & Anchovy Pizza	26	https://images.unsplash.com/photo-1588014164218-d9ecba01aaff?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MTN8fEFuY2hvdnklMjBWaW5haWdyZXR0fGVufDB8fDB8fHww&auto=format&fit=crop&w=900&q=60#	450	3
716345	B	1	https://bit.ly/3oAddoE	1	1
75	Spaghetti with Fried Capers	45	https://www.seriouseats.com/thmb/dsISOa0qDZJbNsuCkaMxjgdWWFk=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc()/__opt__aboutcom__coeus__resources__content_migration__serious_eats__seriouseats.com__2021__02__20210202-spaghetti-puttanesca-melissa-hom-8-65423b5c97b64e30ac7ff6de67d306af.jpg#	450	4
71	Fried Green Tomatoes with Lemon	30	https://www.savoryexperiments.com/wp-content/uploads/2012/11/Fried-Green-Tomatoes-9.jpg#	300	8
79	Artichokes Basted with Butter	45	https://i.guim.co.uk/img/media/42222acc97ed5880cc625292c8262692477ab91d/0_1428_3546_2127/master/3546.jpg?width=1200&height=900&quality=85&auto=format&fit=crop&s=f86f00f782bf05cba84e10d20b2669eb#	200	8
86	Shrimp & Pasta Puttanesca	10	https://marleyspoon.com/media/recipes/2580/main_photos/large/SKU0812_Hero-d7e3bc50e70e67edd14fe37b6f3364a6.jpg#	500	4
39	Radish Salad with Anchovy Sauce	36	https://i.pinimg.com/736x/5e/87/d9/5e87d9361f77863e439804eb2e5f2e3f--anchovy-recipes-salad-recipes.jpg#	200	4
54	Anchovy & Piquillo Pepper Bruschetta	45	https://geniusfood.com/wp-content/uploads/2020/12/Roasted-peppers-with-anchovy-and-capers-2-scaled-e1612179669337.jpg#	180	6
80	Sautéed Radicchio	45	https://www.thespruceeats.com/thmb/I2Gk-4kFoFUqtP0yKgXnfiCn21I=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc()/sauteed-radicchio-recipe-2217562-hero-01-38f5df0cd8944e5abbdde7c3bbb9e8a1.jpg#	150	4
92	Anchovy Bucatini	70	https://static01.nyt.com/images/2020/05/03/dining/03dt-midnight-pasta-horizontal/dt-midnight-pasta-horizontal-superJumbo.jpg#	400	4
53	Anchovy, Little Gem, & Tomato Salad	45	https://media.istockphoto.com/id/1297437821/photo/salad-with-anchovies-or-sardines.jpg?s=612x612&w=0&k=20&c=uuUPAZNc-SE5CHxHPvWGTZAaykvUFGxuGK4sBl79OKw=#	200	4
48	Roasted Red Peppers with Anchovies & Olive Oil	83	https://timesten.imgix.net/assets/img/recipes/2018/09/IMG_2987.jpg?crop=focalpoint&domain=timesten.imgix.net&fit=crop&fm=jpg&fp-x=0.5&fp-y=0.5&h=1500&ixlib=php-3.3.0&q=82&usm=20&w=1500#	300	4
97	Farmers’ Pasta	60	https://i0.wp.com/espressoandlime.com/wp-content/uploads/2021/02/Farmers-Pasta-1.jpeg?resize=700%2C934&ssl=1#	400	8
89	Bigoli en Salsa	50	https://www.sbs.com.au/food/sites/sbs.com.au.food/files/thick-spaghetti-with-onion-and-anchovy-bigoli-in-salsa.jpg#	450	4
64	Sautéed Shrimp with Green Olives, Scallions & Anchovies	25	https://theviewfromgreatisland.com/wp-content/uploads/2017/02/Shrimp-in-lemon-sauce-with-olives-5196-February-20-2017-2.jpg#	350	6
68	Spaghetti with Breadcrumbs	45	https://www.carolynscooking.com/wp-content/uploads/2020/03/63AD2A0A-DCCE-4D2E-9B63-A478EB9B773D-700x1004.jpeg#	400	6
88	Pappardelle with Zucchini	45	https://i.pinimg.com/736x/52/32/6c/52326cee61e1770c433045386f801268.jpg#	450	6
636857	Candied Nuts	45	https://preppykitchen.com/wp-content/uploads/2019/07/candied-pecans-recipe-n.jpg	200	25
634854	Berry Fruit Crumble	45	https://images.unsplash.com/photo-1525093505341-06e6006ff576?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MXx8QmVycnklMjBGcnVpdCUyMENydW1ibGV8ZW58MHx8MHx8fDA%3D&auto=format&fit=crop&w=900&q=60	250	6
632797	Asian Beef	45	https://i0.wp.com/chefsavvy.com/wp-content/uploads/Easy-Mongolian-Beef-1.jpg?resize=665%2C823&ssl=1	400	6
642125	Thai Fried Rice	45	https://hips.hearstapps.com/hmg-prod/images/delish-202101-thaifriedrice-047-ls-1611613162.jpg?crop=0.8888888888888888xw:1xh;center,top&resize=1200:*	550	4
649024	Korean BBQ Beef	45	https://www.tastingtable.com/img/gallery/bulgogi-grilled-beef-ribeye-bbq-korean-asian-chef-chris-oh/image-import.jpg	450	1
655806	Pesto & Yogurt Pasta	45	https://odysseybrands.com/wp-content/uploads/Greek-Yogurt-Pesto-Pasta-4.jpg	550	4
659285	Satay Beef Balls	45	https://hilahcooking.com/wp-content/uploads/2017/06/beef-satay-meatballs.jpg	300	6
649722	Lemon Pepper Steak	45	https://hips.hearstapps.com/hmg-prod/images/lemon-pepper-grilled-rib-eyes-1615571007.jpg?crop=0.497xw:0.745xh;0.0986xw,0.194xh&resize=1200:*	400	36
664643	Vegetarian Burgers	45	https://images.unsplash.com/photo-1520072959219-c595dc870360?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8M3x8VmVnZXRhcmlhbiUyMEJ1cmdlcnN8ZW58MHx8MHx8fDA%3D&auto=format&fit=crop&w=900&q=60	350	3
634404	Basic Risotto	45	https://www.eatingwell.com/thmb/IbDeVkiVaS_m1yk5Fcao8MlOFSI=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc()/EWL-250205-basic-risotto-09-D-e9fc9441a50245909de19f1a05b790f3.jpg	400	2
660133	Roast Chicken	45	https://i2.wp.com/www.downshiftology.com/wp-content/uploads/2022/10/Roast-Chicken-main.jpg	400	4
716300	Plantain Pizza	45	https://www.myrelationshipwithfood.com/wp-content/uploads/2020/04/wskwtvY0zstfiluaWCbf_Groovy_Pizza4079-1.jpg	600	3
634698	Beef Tataki	45	https://cloudfront-ap-southeast-2.images.arcpublishing.com/nzme/7UBQY46BGKVP3Z6SRE2LPD5P5M.jpg	300	4
654435	Pan Seared Salmon	25	https://www.thespruceeats.com/thmb/WRW_ommm7c9nej5PHOnLxZYcMWU=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc()/pan-seared-salmon-recipe-5498576-hero-01-ba14de427f064aacb8763704cd5d56bd.jpg	400	2
633660	Baked Lemon Tart	45	https://images.unsplash.com/photo-1508432310926-5712bcb79944?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8NXx8QmFrZWQlMjBMZW1vbiUyMFRhcnR8ZW58MHx8MHx8fDA%3D&auto=format&fit=crop&w=900&q=60	350	1
662744	Taco Egg Roll	45	https://www.chiselandfork.com/wp-content/uploads/2022/01/taco-egg-rolls-3.jpg	400	8
665574	Yokshire Pudding	45	https://sundaysuppermovement.com/wp-content/uploads/2017/11/yorkshire-pudding-featured.jpg	200	1
\.


--
-- Data for Name: user_info; Type: TABLE DATA; Schema: public; Owner: atip
--

COPY public.user_info (id, username, password, logged_in, first_name, last_name) FROM stdin;
3	User3	1Dqb6ytc	f	NO	NO
4		1Dqb6ytc	f	NO	NO
6	Au	Banana1234	t	Atip	Kajitamkul
7	Test1	Test1naja	f	Test	Tesst
8	test10	Tester10	f	test	test
2	User2	User2	f	\N	\N
5	Vega	Vega1234	f	asd	asd
1	User1	User1	f	\N	\N
\.


--
-- Data for Name: user_log; Type: TABLE DATA; Schema: public; Owner: atip
--

COPY public.user_log (user_id, logged_in_at) FROM stdin;
2	2023-05-27 23:07:24
2	2023-05-27 23:13:34
2	2023-05-27 23:23:35
2	2023-05-27 23:24:35
2	2023-05-27 23:24:39
5	2023-05-27 23:45:36
7	2023-05-28 17:47:47
8	2023-05-28 20:51:58
6	2023-05-28 03:17:40
2	2023-05-27 22:49:06
1	2023-05-30 15:05:49
1	2023-05-30 15:06:32
1	2023-05-30 15:07:20
2	2023-05-27 22:53:09
1	2023-05-30 15:11:11
1	2023-05-30 21:25:54
1	2023-05-30 21:39:33
1	2023-06-04 21:11:41
1	2023-06-04 21:32:08
2	2023-05-27 22:59:18
1	2023-06-04 21:37:24
1	2023-06-04 21:39:36
1	2023-06-04 21:41:25
2	2023-05-27 23:00:14
2	2023-05-27 23:04:50
\.


--
-- Name: added_recipes added_recipes_pk; Type: CONSTRAINT; Schema: public; Owner: atip
--

ALTER TABLE ONLY public.added_recipes
    ADD CONSTRAINT added_recipes_pk PRIMARY KEY (user_id, recipe_id);


--
-- Name: categories categories_pk; Type: CONSTRAINT; Schema: public; Owner: atip
--

ALTER TABLE ONLY public.categories
    ADD CONSTRAINT categories_pk PRIMARY KEY (category_id);


--
-- Name: classify classify_pk; Type: CONSTRAINT; Schema: public; Owner: atip
--

ALTER TABLE ONLY public.classify
    ADD CONSTRAINT classify_pk PRIMARY KEY (category_id, recipe_id);


--
-- Name: favorite_recipes favorite_recipes_pk; Type: CONSTRAINT; Schema: public; Owner: atip
--

ALTER TABLE ONLY public.favorite_recipes
    ADD CONSTRAINT favorite_recipes_pk PRIMARY KEY (user_id, recipe_id);


--
-- Name: ingredients ingredient_pk; Type: CONSTRAINT; Schema: public; Owner: atip
--

ALTER TABLE ONLY public.ingredients
    ADD CONSTRAINT ingredient_pk PRIMARY KEY (id);


--
-- Name: instructions instruction_pk; Type: CONSTRAINT; Schema: public; Owner: atip
--

ALTER TABLE ONLY public.instructions
    ADD CONSTRAINT instruction_pk PRIMARY KEY (id);


--
-- Name: new_recipes new_recipe_pk; Type: CONSTRAINT; Schema: public; Owner: atip
--

ALTER TABLE ONLY public.new_recipes
    ADD CONSTRAINT new_recipe_pk PRIMARY KEY (id);


--
-- Name: recipes recipe_pkey; Type: CONSTRAINT; Schema: public; Owner: atip
--

ALTER TABLE ONLY public.recipes
    ADD CONSTRAINT recipe_pkey PRIMARY KEY (id);


--
-- Name: user_info user_info_pk; Type: CONSTRAINT; Schema: public; Owner: atip
--

ALTER TABLE ONLY public.user_info
    ADD CONSTRAINT user_info_pk PRIMARY KEY (id);


--
-- Name: user_log user_log_pk; Type: CONSTRAINT; Schema: public; Owner: atip
--

ALTER TABLE ONLY public.user_log
    ADD CONSTRAINT user_log_pk PRIMARY KEY (logged_in_at);


--
-- Name: added_recipes added_recipes_recipes_id_fk; Type: FK CONSTRAINT; Schema: public; Owner: atip
--

ALTER TABLE ONLY public.added_recipes
    ADD CONSTRAINT added_recipes_recipes_id_fk FOREIGN KEY (recipe_id) REFERENCES public.recipes(id);


--
-- Name: added_recipes added_recipes_user_info_id_fk; Type: FK CONSTRAINT; Schema: public; Owner: atip
--

ALTER TABLE ONLY public.added_recipes
    ADD CONSTRAINT added_recipes_user_info_id_fk FOREIGN KEY (user_id) REFERENCES public.user_info(id);


--
-- Name: classify categories_recipes_id_fk; Type: FK CONSTRAINT; Schema: public; Owner: atip
--

ALTER TABLE ONLY public.classify
    ADD CONSTRAINT categories_recipes_id_fk FOREIGN KEY (recipe_id) REFERENCES public.recipes(id);


--
-- Name: classify classify_categories_category_id_fk; Type: FK CONSTRAINT; Schema: public; Owner: atip
--

ALTER TABLE ONLY public.classify
    ADD CONSTRAINT classify_categories_category_id_fk FOREIGN KEY (category_id) REFERENCES public.categories(category_id);


--
-- Name: favorite_recipes favorite_recipes_recipes_id_fk; Type: FK CONSTRAINT; Schema: public; Owner: atip
--

ALTER TABLE ONLY public.favorite_recipes
    ADD CONSTRAINT favorite_recipes_recipes_id_fk FOREIGN KEY (recipe_id) REFERENCES public.recipes(id);


--
-- Name: favorite_recipes favorite_recipes_user_info_id_fk; Type: FK CONSTRAINT; Schema: public; Owner: atip
--

ALTER TABLE ONLY public.favorite_recipes
    ADD CONSTRAINT favorite_recipes_user_info_id_fk FOREIGN KEY (user_id) REFERENCES public.user_info(id);


--
-- Name: ingredients ingredient_recipe_id_fk; Type: FK CONSTRAINT; Schema: public; Owner: atip
--

ALTER TABLE ONLY public.ingredients
    ADD CONSTRAINT ingredient_recipe_id_fk FOREIGN KEY (recipe_id) REFERENCES public.recipes(id);


--
-- Name: instructions instruction_recipe_id_fk; Type: FK CONSTRAINT; Schema: public; Owner: atip
--

ALTER TABLE ONLY public.instructions
    ADD CONSTRAINT instruction_recipe_id_fk FOREIGN KEY (recipe_id) REFERENCES public.recipes(id);


--
-- Name: user_log user_log_user_info_id_fk; Type: FK CONSTRAINT; Schema: public; Owner: atip
--

ALTER TABLE ONLY public.user_log
    ADD CONSTRAINT user_log_user_info_id_fk FOREIGN KEY (user_id) REFERENCES public.user_info(id);


--
-- PostgreSQL database dump complete
--

