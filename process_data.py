'''from tokenize import Name
import pandas as pd

df = pd.read_csv("2022-07-05_Final_Output_DMart_ID.csv")
print(df.Category.unique())
print(len(df))
df = df[df['Category'] !='School Suppplies']
df = df[df['Category'] !='Personal Care']
df = df[df['Category'] !='FootWare']
df = df[df['Category'] !='Appliances']
df = df[df['Category'] !='Home & Kitchen']
df = df[df['Category'] !='Packaged Food']
print(len(df))
#print(df['Item Name'].unique())'''

ingredient_cleaning_dict = {'Premia Sugar':'Sugar','Premia Cow Ghee Pouch':'Cow Ghee','Premia Refined Rice Bran Oil':'Rice Bran Oil',
'Premia Badam (Almonds)':'Almond','Premia Groundnut':'Groundnut','Premia Poha Jada':'Flattened rice',"Premia Jeera":"Cumin",'Premia Regular Kaju (Cashews) - 320':'Cashews',
'Premia Sabudana':'Sago','Premia Akrod Magaj (Walnut Kernels)':'Walnut Kernels','Premia Green Elaichi':'Cardamom','Premia Kismis Indian (Raisins)':'Raisin',
'Premia Dry Coconut':'Coconut','Premia Pista Salty (Pistachio)':'pistachio','Premia Black Pepper':'Black Pepper','Premia Dhaniya':'Coriander','Premia Kaju Tukda (Cashews)':'Cashews',
'Premia Kashmiri Chilli Powder Deluxe':'Chilli Powder','Premia Pista Plain (Pistachios)':'Pistachios','Premia Extra Strong Hing Powder':'asafoetida',
'Premia Badishep':'Fennel ','Premia Rai':'Black Mustard Seeds','Premia Kashmiri Chilli Powder':'Chilli Powder','Premia Mixed Dry Fruits':' Dry Fruits','Premia Cassia Taj':'Premia Cassia Taj',
'Premia Cassia Taj':'Cassia Cinnamon','Premia Haldi Powder Deluxe':'turmeric','Premia Yellow Hing Powder':'asafoetida',
 'Premia Dhania Powder Deluxe':'Coriander', 'Premia Ajma' :'Celery','Premia Kaju':'Cashew', 'Premia Emli':'Tamarind',
 'Premia Rai Small':'Mustard' ,'Premia Poha Patla':'Flattened rice', 'Premia Cashew Broken':'Cashew',
 'Premia Til White':'sesame', 'Premia Coconut Powder':'Coconut','Premia Mamra Badam':'almond',
 'Premia Soyawadi':'soy bean', 'Premia Lukhnowi Badishep':'Fennel','Premia Khas Khas':'poppy seeds',
 'Premia Kaju Special (Cashews) - 240':'Cashew','Premia Green Elaichi Economy':'Cardamom',
 'Premia Star Anise (Badiyan)':'European anise','Premia Guntur Chilli':"Chilli",
 'Premia Roasted Badishep': 'Fennel','Premia Lawang':'clove ','Premia Kismis Black (Raisins)':'Raisin',
 'Premia Dhaniya Dal':'roasted coriander ','Premia Red Dried Dates (Kharik)':'Dates',
 'Premia Poha Basmati': 'Flattened rice','Premia Red Chilli Powder':'Chilli','Premia Kasoori Methi':'Dried fenugreek leaves',
 'Premia Methi':"fenugreek", 'Premia Sabja':' sweet basil seeds','Premia Jeera Powder Deluxe':'Cumin powder',
 'Premia Sabudana Small' :'tapioca pearl','Premia Black Pepper Powder':'Piper nigrum',
 'Premia Yellow Chana':'yellow gram','Premia Shaha Jeera':'Cumin','Premia Kismis Black Seedless':'Raisin',
 'Premia Jardalu':'apricot', 'Premia Alsi':'Linseed','Premia Bedgi Chilli': 'Chilli','Premia Dry Apricot':'Apricot',
 'Premia Chilli Kashmiri':'Chilli' ,'Premia Garam Masala Powder Deluxe':'Allspice and Cumin',
 'Premia Jaipatri (Mace)':'Mace', 'Premia Grated Dry Coconut':'Coconut',
 'Premia Anjeer (Figs)':'Figs','Premia Tej Patta':'Indian bay leaf', 'Premia Masala Elaichi':'Cardamom',
 'Premia Dhania Powder':'Coriander', 'Premia Sugar Crystals (Khadi Shakkar)':'clumps of sugar',
 'Premia Dhania Jeera Mix Khandela':'Cumin','Premia Jaifal': 'nutmeg',
 'Premia Kismis Selected' :"Raisin",'Premia Amsul Wet Kokam':"Garcinia indica ",
 'Premia Mini Soya Chunks':"textured soy protein",'Premia Kaju (210) Premium':'Cashew',
 'Premia Malwani Masala Deluxe':"Allspice and Cumin" ,
 'Premia Reshampatti Chilli Khandela':"Chilli", 'Premia Til Black':"Til",
 'Premia Black Dried Dates (Kharik)':"Dates", 'Premia Kokam Rind Lonavala':"Garcinia indica",
 'Premia Eating Soda':"Baking soda",'Premia Chilli Guntur Stemless':"Chilli",
 'Premia Ginger Powder':"Ginger ", 'Premia Kalvanji':"black cumin", 'Premia Dry Ginger (Sunth)':"Ginger",
 'Premia Dinkh (Edible Gum)':"dinkh ",'Premia Nimbu Phool (Citric Acid)':"Citric Acid",
 'Premia Dagad Phool (Black Stone Flower)':"Parmotrema perlatum" ,'Premia Charoli' :"almond-flavoured seeds",
'Premia Halim':"Garden cress seeds",'Premia Akrod Whole':"Walnut",  'Tur Dal Latur':"Pigeon pea", 'Moong Dal':"Green gram dal", 'Chana Dal':"Yellow lentil ",'Udid (Urad) Dal':"Black lentils",
'Tur Dal Premium Gujarat':"Pigeon pea",'Masoor Dal':"Red Lentil",'Vatana White':"dried white peas",'Masoor Whole':"brown lentils",'Udid (Urad) Whole':"black gram", 'Rajma White':"kidney beans",
 'DMart Healthy Choice Unpolished Toor Dal':"pegeon pea","Red Gram Split":"pegeon pea",'Daliya':"porridge ",
 'Rajma Kashmiri Red':" dark red kidney beans" ,'Vatana Green':"peas", 'Mix Dal':" ", 'Chowli Big':"black-eyed peas ",
 'Chowli Premium':"black-eyed peas",'Chowli Small':"black-eyed peas",'Udid (Urad) Dal Chilti':"black gram lentils",
 'DMart Healthy Choice Unpolished Moong Dal':"Green gram lentils",'Udid (Urad) Black Whole':"Black Gram Whole",
 'Rajma Red Small' :"kidney beans",'Chana Green':"chick pea ",'Chowli Red':"black-eyed peas",
 'Vatana Black':"black peas",'DMart Healthy Choice Unpolished Chana Dal':"split chickpea lentils",
 'Kulith (Horse Gram)':"Macrotyloma uniflorum", 'Ranguni Wal':" Field beans",'Wal Papdi':"field beans",
 'Premium Jaggery':"Jaggery",'Keshar Premium Natural Jaggery Jar':"Jaggery", 'Jaggery':"Jaggery",
 'Wada Kolam Sorted Rice':"Rice",'Lachkari Silky Kolam Sorted Rice':"Rice",
 'HMT Kolam Sorted Rice':"Rice", 'Basmati Rice Mogra':"Rice", 'Ambemohar Rice':"Rice" ,'Idli Rice':"Rice",
 'Eco Kolam Jirasar Sorted Rice' :"Rice",'Rice Pulav Basmati':"Rice",
 'Basmati Rice Mini Mogra (Broken)':"Rice",'Basmati Rice':"Rice",
 'GB Surti Kolam Sorted Rice':"Rice",
 'Biryani Rice' :"Rice", 'Rice Tibar Basmati':"Rice",
 'Red Rice':"Rice", 'Rice Basmati Wand':"Rice", 'Mogra Basmati Rice':"Rice" ,'IR Boiled Rice':"Rice",
 'Masoori Boiled Rice':"Rice", 'Miki Maize (Makai) Poha':"maize flakes",
'Makhana (Foxnuts)':"FoxNuts",'Date Crown Fard (Khajur)':"Date",
 'Emperor Dates - Deseeded Black Dates (Khajur)':"Dates",
 'Date Crown Khenaizi (Khajur)':"Date", 'Falcon UAE Dates Seedless (Khajur)':"Date",
 'Emperor Royal Peacock Seeded Dates (Khajur)':"Date", 'Date Crown Bumaan Dates':"Date",
 'Akrod (Walnut) Whole':"walnut", 'Falcon Aqaba Dates':"Date", 'Falcon UAE Dates Seeded':"Date",
 'Falcon Zahdi Dates Seeded' 'Amchur Powder' 'Wheat Lokwan (Lokvan)':"wheat",
 'Wheat Sihore':"Wheat",'Rava':"semolina", 'Besan':"Gram Flour", 'Maida':"refined wheat flour", 'Jawar (Sorghum) Solapur':"Sorghum",
 'Lapsi Rava Small Daliya':"Porridge",'Lapsi Rava / Daliya':"cracked wheat",
 'Nachni':"finger millet" ,'Rice Atta' :"Rice Atta",'Idli Rava':"cracked wheat",'Wheat MP Sihore Premium':"wheat",

 'Swaad Refined Sunflower Oil':"Sunflower oil",'Nutraj California Almonds (Badam)':"Almonds",
 'Tata Sampann Chana Dal' :"split chickpea lentils",'Nutraj Almond' 'Satyam Rajma Pink':"kidney beans",
 'KMK Almond Mamra (Badam)':"Almond",'Satyam Rajma Sharmili':"kidney beans", 'Satyam Chana Dal':"split chickpea lentils",
 'KMK Almond American (Badam)':"Almond",'Tata Sampann Orgnc Unpol Rajma Red':"Kidney Beans",
 'Nutraj Cashews':"Cashew",'Tata Sampann Moong Dal':"Green gram lentils", 'Kalbavi Cashews (Kaju)':"Cashew",
 'Kokan Gem Goa Cashew Classic (Kaju)':"Cashew",
 'Kokan Gem Goa Cashew Premium (Kaju)':"Cashew", 'Tata Sampann Moong Chilka':"Green gram split",
 'Satyam Moong Dal':"Green gram lentils",'Tata Sampann 100% Organic Unpolished Moong Dal':"Green gram lentils",
 'KMK Cashew Nut (Kaju)' :"cashew",'24 Mantra Organic Moong Dal':"Green gram lentils" ,'Amul Butter':"Butter",
 'Society Tea':"Tea",'Wagh Bakri Premium Leaf Tea Pouch':"Tea",
 'Brooke Bond Red Label Tea':"Tea", 'Tata Tea Agni':"Tea",
 'Brooke Bond Red Label Natural Care Tea' :"Tea",'Girnar Royal Cup Tea':"Tea",
 'Tata Tea Premium':"Tea", 'Taj Mahal Tea':"Tea", 'Tata Tea Gold':"Tea",
 'Society Masala Flavour Tea Pouch':"Tea" ,'Wagh Bakri Navchetan Tea':"Tea",
'Tetley Green Tea Lemon & Honey':"Green tea",
 'Brooke Bond Taaza Tea' :"Tea",'Mother Dairy Pasteurized Butter':"Butter",
 'Tata Tea Gold Care':"Tea",
 'Lipton Green Tea - Honey Lemon' :"green tea",'Amul Garlic & Herbs Buttery Spread':"Buttery Spread",
 'Tata Tea Teaveda':"Tea", 'Girnar Detox Green Tea Desi Kahwa':"green tea",
 'Amul Butter School Pack':"Butter", 'Brooke Bond Taj Mahal Tea':'Tea',
 'Nutralite Fat Spread UKE':"Nutralite Fat",'Amul Butter Unsalted':'Butter',
 'Girnar Jumbo Gulabi CTC Leaf Tea' :"Tea",'Lipton Green Tea - Pure & Light':"Green tea",
 'Goodricke Super Cup Tea':'Tea', 'Girnar Masala Instant Premix Chai':"Tea",
 'Lipton Pure & Light Green Tea':'Tea', 'Amul Lite Milk Fat Bread Spread':"Milk fat fread",
 'Girnar Cardamom Instant Premix Chai':"Tea",
 'Tetley Ginger Mint Lemon Green Tea':"grean tea",
 'Tea Country Honey & Lemon Green Tea':"Tea",'President Premium Butter Salted':'Butter',
 'Amul White Butter Unsalted':"Butter", 'Lipton Green Tea - Lemon Zest':"Tea",
 'Tetley Long Leaf Green Tea Powder' :"Green tea",'Wagh Bakri Green Tea Honey Lemon':'Tea',
 'Organic India Tulsi Green Tea - Classic':'Grean tea',
 'Organic India Tulsi Green Tea - Lemon Ginger':"Green tea",
 'Wagh Bakri Premix Instant Tea':"Tea",'Arbor Treat Assam CTC Tea':"Tea",
 'President Premium Butter Unsalted':"Butter",'Wagh Bakri Green Tea Tulsi':"Green tea",
 'Wagh Bakri Premix Masala Instant Tea' :'Tea','Tea Country Original Green Tea':"Green Tea",
 'Wagh Bakri Premix Elaichi Instant Tea':"Tea" ,'Wagh Bakri Green Tea Mint':"Green tea",
 'Wagh Bakri Green Tea' :'green tea','Society Cleanse Detox Kahwa Green Tea Premix':"Green tea",
 'TGL Co. Kashmiri Kahwa Green Tea':"Green tea",'TGL Co. Mogo Mogo Green Tea':'Green tea',
 'Twinings Green Tea & Lemon':"Green tea",'Twinings Green Tea & Mint':'Green tea',
 'Society Premium Tea' :"Tea",'Amul Taaza Toned Milk':'Toned Milk',
 'Nandini Good Life Toned Milk':"Toned Milk", 'Go Double Toned Milk':' Toned Milk',
 'Amul Slim-n-Trim Skimmed Milk':"  Milk", 'Nestlé A+ Nourish Toned Milk':"Toned Milk",
 'Amul Kool Kesar Milk':"Milk",'Amul Kool Badam Milk' :"Milk",'Amul Kool Cafe Milk':"Milk",
 'Amul Kool Elaichi Milk':"Milk",'Epigamia Milkshake Chocolate':"Milk",
 "Cavin's Chocolate Milkshake" :"Milk",'Amul Kool Rose Milk':"Milk",
 'Amul Lactose Free Milk':'Milk', "Cavin's Vanilla Milkshake":"Milk",
 'Epigamia Milkshake Strawberry':'Milk','Sofit Soya Drink Naturally Sugar Free':'Milk Powder',
 'Raw Pressery Almond Milk Plain (Unsweetened)':'Milk',
 'Sofit Soya Drink Chocolate' 'Lipton Green Tea - Tulsi Natura':'Green tea',
 'Sofit Soya Drink Vanilla':'Soya drink','Tea Country Tulsi Green Tea':"Green Tea",
 'Chitale Flavoured Milk Butterscotch':" Flavoured Milk",'Amul Basundi Kesar Elaichi':'Elaichi',
 'Arbor Qahwa Green Tea With Herbs & Spices':"Green tea",
 'Sofit Soya Drink Kesar Pista':"Kesar Pista", 'Chitale Flavoured Milk - Coffee':" Flavoured Milk",
 'Chitale Flavoured Milk Rose':"Milk Rose" ,'Amul Processed Cheese Cubes':'Cheese ',
 'Amul Processed Cheese' :"Cheese",'Gowardhan Cheese Slice - 28 Slices':'Cheese',
 'Amul Processed Cheese Block':"Cheese",'Amul Cheese Slices':"Cheese",
 'Britannia Cheese Slices':"Cheese", 'Gowardhan Processed Cheese Slices':"Cheese",
 'Amul Mozzarella Diced Pizza Cheese (Frozen)':'Cheese',
 'Amul Diced Mozzarella & Cheddar Cheese Blend (Frozen)':"Cheese",
 'Gowardhan Processed Cheese' :"Cheese",'Amul Cheese Spread Plain':"Cheese Spread",
 'Britannia Cheese Block':'Cheese','Britannia Cheese Cubes':'Cheese Cubes',
 'Britannia Cheeza Pizza Cheese':"Cheese", 'Tetley Green Tea Ginger Mint & Lemon':"Green tea",
 'Amul Easy To Grate Processed Cheese':"Cheese","D'lecta Cheese Slices":"Cheese",
 'Amul Diced Blend Cheese':"Cheese", 'Gowardhan Go Cheese Slices - Plain':'Cheese',
 'Tetley Classic Immune Green Tea':"Green tea" ,"D'lecta Shredded Mozzarella Cheese": "Cheese",
 "D'lecta Cheese Cubes":"Cheese Cubes",'Mother Dairy Cheese Cubes':"Cheese Cubes",
 'Mother Dairy Cheese Slices':"cheese Slices" ,'Amul Mozzarella & Cheddar Pizza Cheese':"Cheese",
 "D'lecta Cream Cheese":"Cheese", "D'lecta Processed Cheese Block":"Cheese",
 "D'lecta Natural Feta Salad Cheese":"Cheese", 'Gowardhan Go Pizza Cheese':"Cheese",
 "D'lecta Cheese Spread":"Cheese", "D'lecta Natural Cheddar Cheese":"Cheese",
 'Amul Mozzarella Pizza Cheese (Frozen)':"Cheese",
 "D'lecta Frozen Shredded Mozzarella Cheese":"Cheese",
 'Gowardhan Processed Cheese Angles':"Cheese",
 "D'lecta Natural Cheddar Cheese Slices":"Cheese",
 'Wagh Bakri Shudh Kahwa Green Tea':"Green tea",'Organic Tulsi Green Tea Classic':"Green tea",
 'Organic Tulsi Ginger Turmeric':"Ginger Turmeric" ,'Twinings Green Tea Lemon & Honey':'Green tea',
 'Tea Culture Of The World Soothing Chamomile Exotic Tea':'Tea',
 'Tea Culture Of The World Moroccan Mint Exotic Tea':"tea",
 'Twinings Pure Green Tea':"Green tea",
 'Tea Culture Of The World Flowery Bouquet Exotic Tea':'Tea',
 'Tea Culture Of The World Kashmiri Kahwa Exotic Tea':'Tea',
 'Tea Culture Of The World Tulsi Ritual Exotic Tea':'Tea',
 'Twinings Darjeeling Loose Leaf Tea':'tea','Bru Instant Coffee':'coffee',
 'Nescafé Classic Coffee':'coffee','Le Café 100% Pure Instant Coffee':'Coffee',
 'Nestlé Everyday Dairy Whitener':'Dairy Whitener','Gowardhan Paneer Classic Block':'Paneer',
 'Amul Masti Spiced Buttermilk':'Buttermilk','Nescafé Sunrise Coffee':"Coffee",
 'Amul Fresh Paneer':'Paneer','Nescafé Classic Coffee Jar':'Coffee', 'Amul Fresh Cream':"Cream",
 'Yakult Probiotic Health Drink':'Health Drink', 'Aabad Malai Paneer':'Paneer',
 'House Instant Coffee' :"coffee",'Amul Mithai Mate Sweetened Condensed Milk':'Milk',
 'Nestlé Milkmaid':'Milkmaid', 'Nescafe Gold Blend Coffee Jar':"Coffee",
 'Amulya Dairy Whitener Milk Powder':'Milk Powder' ,'Chitale Fresh Paneer':'Paneer',
 'Le Cafe Coffee Jar' :"coffee",'Continental Xtra Coffee Jar':'coffee', 'Prabhat Malai Paneer':"Paneer",
 'Amul Malai Paneer (Frozen)':"Paneer", 'Amul Frozen Rasmalai':'Rasmalai',
 'Continental Xtra Instant South Blend Coffee':"Coffee",
 "Hershey's Chocolate Milk Shake":'Milk Shake','Colombian Brew Instant Coffee Original':'Coffee',
 'Id Natural Paneer':"Paneer", 'Davidoff Coffee Espresso Intense':'Coffee',
 'Epigamia Milkshake Vanilla':"Milkshake Vanilla",'Cothas Coffee Speciality Blend':'Coffee',
 'Davidoff Coffee Rich Aroma':"Coffee","D'lecta Dairy Cream":'Cream',
 'Colombian Brew Instant Coffee Nutty Hazelnut':'Coffee','Amul Mango Lassi':'Mango Lassi',
 'Le Café Instant Coffee':'Coffee', 'Amul Rose Lassi':'Rose Lassi',
 'Colombian Brew Cappuccino Coffee Premix' :"Coffee",'Amul Lassi':"Lassi",
 'Nescafe Chilled Latte Coffee & Milk Beverage':'Coffee & Milk Beverage',
 'Colombian Brew Double Chocolate Mocha Coffee Premix' :'Chocolate Mocha Coffee','Go Buttermilk':" Buttermilk",
 'Nescafe Cappuccino Flavour Instense Café':"Coffee",
 'Nescafe Iced Latte Flavoured Can':"Coffee",
 'Colombian Brew Hazelnut Coffee Premix':'Coffee',"Cavin's Strawberry Milkshake":"Milkshake",
 'Yakult Light Health Drink':' Health Drink',
 'Colombian Brew Instant Coffee Double Chocolate Mocha':'Chocolate Mocha Coffee',
 'Nescafe Cappuccino Flavour Can':'Coffee',
 'Colombian Brew Vanilla Caramel Coffee Premix':'coffee',
 "Hershey's Milkshake Strawberry Flavour":'Milkshake',
 "Hershey's Milkshake Cookies N Cream Flavour":'Milkshake','Mother Dairy Masala Chach':"buttermilk",
 'ID Instant Filter Coffee Bold':'Coffee', 'Chitale Buttermilk':'Buttermilk',

 'Colombian Brew Instant Coffee Wild Vanilla':'Coffee',
 'ID Instant Filter Coffee Strong':'Coffee','Davidoff Coffee Fine Aroma':'Coffee',
 'Colombian Brew Instant Coffee Creamy Caramel':'Coffee',
 "D'lecta D'licia Whip Topping":'Whip Topping','Continental Speciale Coffee Pouch':"Coffee",
 'Davidoff Coffee Crema Intense':"Cream","D'lecta Dairy Whipping Cream":"Cream",
 'Raw Pressery Milkshake Cold Coffee' 'Amul Kesar Elaichi Basundi':"Elaichi",
 'TGL Co. Euphoria Instant Coffee Powder':'Coffee',
 'Nescafé Classic Black Roast Coffee Jar':"Coffee",'Chitale Keshar Flavoured Milk':"Flavoured Milk",
 'Colombian Brew Green Coffee':'Green coffee' ,'ITC Sunbean Beaten Caffe Strong Jar':"Coffee",
 'Nescafé All In One Coffee' :'Coffee',"Haldiram's Matka Jhatka Masala Chaas":"Butter milk",

 'Pediasure Nutritional Powder - Premium Chocolate Flavour':'Nutritional Powder',
 'Protinex Original Health Drink':"Protinex",
 'Protinex Chocolate Flavour Health Drink Tin':"Protinex",
'Protinex Original':'Protinex',
 'Horlicks Health & Nutrition Drink Refill - Chocolate':"Chocolate",
'Complan Royal Chocolate':'Chocolate' ,'Protinex Vanilla Flavour Health Drink':'Protinex',
'Britannia Thick Dahi':'curd','Amul Masti Dahi':'curd',
 'Cadbury Hot Chocolate Drinking Powder':'curd', 'ID Creamy Thick Curd - Dahi':'curd',
 'Pediasure Nutritional Powder - Vanilla Delight Flavour':"Nutritional Powder",
 'Complan Kesar Badam Health Drink':'Health Drink',
 "Hershey's Natural Unsweetened Cocoa Powder":"Cocoa Powder",'Amul Premium Dahi':'curd',
 'Chitale Dahi' :'curd',
 'Christopher Dark Cocoa Powder For Baking & Hot & Cold Drinks':'Cocoa Powder',
 'Christopher Cocoa Original Drinking Cocoa':'Cocoa ',
 'Horlicks Chocolate Delight Flavour Jar' 'Blue Bird Cocoa Powder':'Cocoa Powder',
 'Mirinda Orange':'Mirinda Orange' , 'Thums Up':'Thums Up','Sprite':'Sprite','Pepsi':'Pepsi' ,'Fanta Orange Flavour':"Fanta",
 'Bisleri Club Soda' :'Bisleri Club Soda','7 Up':'7 Up' ,'Coca-Cola' :'Coca-Cola','Limca':"Limca",
 'Xotik Jeeru Jeera Masala Drink':'Jeera Masala Drink',
 'Heineken 0.0% Non-Alcoholic Can' :'Non-Alcoholic Can',"Duke's Club Soda":"Club Soda",
 'Coolberg Assorted Non-Alcoholic Beer' :'Assorted Non-Alcoholic Beer','Appy Apple Juice Drink':'Apple Juice',
 'Epigamia Low Fat Greek Yogurt Blueberry':'Yogurt Blueberry',
 'Cravova Green Apple Mojito':'Green Apple Mojito',
 'Epigamia Low Fat Greek Yogurt Natural':'Yogurt Natural',
 'Bisleri Limonata - With Lime Juice':"Lime Juice", 'Coca-Cola No Sugar Bottle':'Coca-Cola',
 'Coke Zero Sugar':'Coke','Cravova Watermelon Mojito':'Watermelon Mojito',
 'Coolberg Peach Non-Alcoholic Beer':' PeachNon-Alcoholic Beer',
 'Epigamia Low Fat Greek Yogurt Alphonso Mango':'Yogurt Alphonso Mango', 'Cravova Fresh Lemonade':'Lemonade',
 'Epigamia Low Fat Greek Yogurt Wild Raspberry':"Yogurt Wild Raspberry",'Coca-Cola Tin':'Coca-Cola',
 'Kingfisher Radler Lemon Non-Alcoholic Can':"Lemon Non-Alcoholic Can",
 'Coolberg Ginger Non-Alcoholic Beer':' Ginger Non-Alcoholic Beer',
 'Kingfisher Radler Mint Non-Alcoholic Can':' Mint Non-Alcoholic Can',
 'Epigamia Greek Yogurt Zero Added Sugar Strawberry':'Epigamia Greek Yogurt Strawberry ',
 
 'Epigamia Greek Yogurt Smoothie - Blueberry':"Epigamia Greek Yogurt Blueberry",
 'Bisleri Fonzo - Mango With Fizzz':'Mango With Fizzz',
 'Schweppes Original Ginger Ale':' Ginger Ale','Maaza Mango Drink' :'Maaza Mango','Slice Mango Drink':'Slice Mango',
  'Minute Maid Pulpy Orange Juice':'Orange Juice','B Natural Mixed Fruit Beverage':'Fruit Beverage', 'Real Fruit Power Litchi':'Fruit Power Litchi',
 'B Natural Guava Fruit Beverage':' Guava Fruit Beverage','Real Fruit Power Guava':'Fruit Power Guava','B Natural Litchi Fruit Beverage':'Litchi Fruit Beverage',
 'Raw Pressery Coconut Water':'Coconut Water','Chitale Full Cream Shrikhand Amba':' Cream Shrikhand Amba',
 'Paper Boat Aamras Drink':'Aamras Drink', 'Tropicana Guava Delight':'Guava Delight',
 'Real Fruit Power Apple':" Power Apple", 'Amul Amrakhand' :"Amrakhand",'Amul Shrikhand Badam Pista':'Badam Pista','Tropicana Apple Delight':'Apple Delight',
 'Paper Boat Chilli Guava Drink':'Guava Drink', 'Tropicana Orange Delight':'Orange Delight',
 'Tropicana Litchi Delight':"Litchi Delight",'Paper Boat Alphonso Aam Drink':"Mango drink",
 'Amul Shrikhand Mango':" Mango", 'Amul Shrikhand Elaichi':"Elaichi",
 'Paper Boat Jaljeera Drink':"Jaljeera Drink", 'Chitale Full Cream Shrikhand Badam Pista':'Badam Pista',
 'Raw Pressery Orange Juice':"Orange Juice", 'Amul Shrikhand Kesar':'Shrikhand Kesar',
 'Paper Boat Anar Drink':" Anar Drink", 
 'Baidyanath Amla Juice':"Amla Juice", 'Raw Pressery Pomegranate Juice':"Pomegranate Juice",
 'Baidyanath Aloevera Juice':"Aloevera Juice", 'Raw Pressery Sugarcane':"Sugarcane",
 'Baidyanath Karela Jamun Juice':"Karela Jamun Juice", 'Glucon-D Instant Energy Orange':"Glucon-D",
 'Red Bull Pack':'Energy Drink' ,'Glucon-D Instant Energy Nimbu Pani':"Glucon-D",
 'Monster Energy Drink Tin':"Energy Drink" ,'Red Bull Energy Drink':"Energy Drink",
 'Glucon-D Instant Energy Plain':"Glucon-D", "O'cean Natural Power Energy Drink":"Energy Drink",
  'Budweiser Beats Energy Drink':"Energy Drink",
 'Cipla Prolyte ORS - Orange Flavour':"Prolyte ORS-Orange", 'Cipla Prolyte ORS - Apple Flavour':"Prolyte ORS-Apple",
 'Guruji Kesaria Thandai':"Cannabis" ,'Kokan Gem Kokam Syrup':"Syrup", "Mala's Rose Syrup":"Syrup",
 "Hershey's Chocolate Syrup":"Syrup" ,'Konkan Amrutam Kokam Syrup':"Syrup",
 'Home Made Real Variyali Syrup':"Syrup",'Home Made Rose Falooda Syrup':"Syrup", 'Home Made Masala Shikanji Syrup':"Syrup",
 'Monin Mojito Mint Flavoured Syrup':"Syrup",'Home Made Anjeer Kesar Fruit Squash':"Anjeer Kesar Fruit Squash", 'Guruji Rose Sharbat':'Rose Sharbat',
 'Monin Green Apple Flavoured Syrup':"Syrup", 'Monin Vanilla Flavoured Syrup':"Syrup",'Tang Orange Instant Drink Mix Powder':"Tang Powder",
 'Tang Lemon Instant Drink Mix Powder':"Tang Powder",'Tang Mango Instant Drink Mix Powder':"Tang Powder", 'Rasna Insta Orange Powder':"Rasna Powder",
 'Rasna Insta Mango Powder':"Mango Powder", 'Jalani Jaljira' :"Jaljira",'Jalani Nimbu Pani':'Nimbu Pani','Jalani Gulaab Sharbat Mix':"Gulaab Sharbat" ,'Weikfield Drinking Chocolate':"Chocolate",
 'Bisleri Packaged Drinking Water':"Water" ,'Bisleri Water':" Water",'Tata Copper Plus Water':" Water", 'Perrier Carbonated Mineral Water':" Water",
 'Fresh Watermelon (Tarbooj)':'Watermelon' ,'Fresh Pomegranate (Anar)':'Pomegranate','Apple Royal Gala (Seb)':"Apple", 'Fresh Pear (Nashpati)':"Pear",
 'Fresh Apple (Seb) Kinnaur':"Apple" ,'Fresh Muskmelon (Kharbooja)':"Muskmelon",'Fresh Banana (Kela) Elaichi':"Banana" ,'Fresh Orange (Santra) Imported':'Orange',
 'Apple Red Delicious':"Apple", 'Fresh Kiwi: 3 Pieces':"Kiwi" ,'Fresh Papaya (Papita)':"Papaya",'Sonaka Fresh Grapes (Draksha)':"Grapes",'Fresh Apple Green':"Apple", 'Fresh Raw Mango':"Raw Mango",
 'Fresh Sweet Lime (Mosambi)':"Sweet Lime",'Fresh Dragon Fruit (Pitaya)':"Dragon",
 'Fresh Guava (Peru)':"Guava" ,'Fresh Indian Gooseberry (Amla)':"Gooseberry",
 'Sweet Tamarind (Thailand)':"Tamarind" ,'Fresh Apple Fuji':"Apple",
 'Fresh Apple (Seb) Washington':"Apple" ,'Anjeer (Figs)':"Anjeer", 'Fresh Sapota (Chikku)':"Sapota",
 'Robusta Banana (Kela)':"Banana",'Fresh Pineapple (Ananas)':"Pineapple",
 'Raw Banana (Kela) Madras':"Banana" ,'Fresh Mango - Dasheri':"Mango",'Mango Langra':"Mango",
 'Mango Neelam':"Mango", 'Mango Chaunsa':"Mango", 'Indian Peach':"Peach", 'Plum Indian':"Pulm" ,'Onion':"Onion",
 'Fresh Potato (Aloo)':"Potato", 'Freshezza Frozen Green Peas':"Peas",
 'Godrej Yummiez Frozen Green Peas':"Peas" ,'Coconut':'Coconut', 'Garlic (Lahsun)':"Garlic",
 'Fresh Tomato (Tamaatar)':"Tomato" ,'Godrej Yummiez Green Peas':"Peas",
 'Fresh Lemon (Nimboo)':"Lemon", 'Ginger (Adrak)':"Ginger" ,'Fresh Button Mushrooms':"Mushrooms",
 'Tender Coconut':"Coconut", 'Fresh Cucumber White (Safed Kakdi)':"Cucumber",
 'Fresh Lady Finger (Bhendi)':"Lady Finger", 'Cauliflower (Ful Gobi)':"Cauliflower",
 'Fresh Capsicum Green (Shimla Mirch)' :"Capsicum Green",'Safal Frozen Mixed Vegetables':"Sofal",
 'Fresh English Carrot (Gajar)':"Carrot" ,'Sweet Potato (Ratala)':"Potato",
 'Fresh Groundnut (Mungfali)':"Groundnut" ,'Malgudi Garlic Peeled':"Garlic",
 'Sambhar Onion (Madras Onion)':"Onion", 'Fresh Avocado':"Avocado",
 'Fresh Green Chilli (Mirchi)' :"Green Chilli",'Bottle Gourd (Dudhi)':"Gourd",
 'Fresh Green Cucumber (Kakdi)':"Cucumber" ,'Fresh Brinjal (Bharta Baingan)':"Branjal",
 'Fresh Beetroot (Chukandar)':"Beetroot", 'Cabbage (Patta Gobi)':"Cabbage", 'Fresh Sweet Corn':"Corn",
 'Drumsticks (Shevgyacha Shenga)' :"Drumsticks",'Fresh Capsicum Red & Yellow':"Capdicum",
 'Fresh Baby Potato (Dum Aloo)' :"Potato",'Fresh Elephant Foot Yam (Suran)':"Elephant Foot Yam",
 'Fresh Baby Corn':"Corn", 'Bitter Gourd (Karela)':"Bitter Ground" ,'Fresh Colocasia (Arbi)':"Colocasia",
 'Fresh Broccoli':"Broccoli", 'French Beans (Faliya)':"French Beans",
 'Fresh Brinjal Round (Kateri Wangi)':"Brinjal", 'Fresh Sponge Gourd (Ghosale)':"Sponge",
 'Fresh Disco Pumpkin (Kaddu/Bhopla)':"Pumokin", 'Fresh Brinjal Small':"Brinjal",
 'Fresh Cluster Beans (Gavar)':"Cluster Beans",'Fresh Sprouts Mixed Gram':"Sprouts", 'Zucchini Green':"Zucchini Green",
 'Malgudi Fried Rice/Noodles Mix':"Malgudi Fried Rice", 'Fresh Lemon Grass':"Lemon Grass",
 'Fresh Cabbage - Red' :"Cabbage",'Broad Beans (Papadi)':"Board Beans" ,'Zucchini Yellow':"Zucchini Yellow",
 'Malgudi Sambar Mix':"Sambar Mix" ,'Malgudi Coconut Chutney':"Coconut Chutney" ,'Malgudi Sugarcane Cubes':"Sugarcane",
 'Malgudi Thai Curry Mix Vegetables':"Thai Curry", 'Malgudi Biryani/Pulav Mix':"Biryani",
 'Fresh Sprouts Moong Green':"Fresh Sprouts Moong Green", 'Fresh Sprouts Mataki':"Fresh Sprouts Mataki",
 'Malgudi Green Peas Shelled':"Peas",'Malgudi Pumpkin Cubes':"Pumpkin Cubes", 'Malgudi Yam Cubes':"Yam Cubes",
 'Malgudi Oondhiyo Mix':"Oondhiyo" ,'Fresh Sprouts Chana Brown':"Chana", 'Malgudi Green Masala':"Green Masala",
 'Fresh Tomato - Cherry':"Tomato", 'Fresh Curry Leaves (Kadi Patta)':"Curry Leaves",
'Matki':"Matki",
}


def comparing_ingredient_cleaning_dict(raw_name):
    if raw_name in ingredient_cleaning_dict.keys():
        return ingredient_cleaning_dict[raw_name], True
    else:
        return raw_name, False




def converstion(quantity,price):
    price=float(price)
    try:
        num_weight=float(quantity.split()[0])
    except:
        num_weight=float(quantity.split()[0][2:])
    unit=quantity.split()[1]

    try:
        if unit=="gms":
            num_weight=quantity.split()[0]
            num_weight=num_weight
            price_1_gram=price/num_weight
            price=price_1_gram*1000
            quantity=1
    #return price,quantity

        elif unit=="Kg" or "Kgs":
            num_weight=quantity.split()[0]
            price=price/num_weight
            quantity=1

        elif unit=="ml":
            num_weight=quantity.split()[0]
            price_1_gram=price/num_weight
            price=price_1_gram*1000
            quantity=1

        elif unit=="Liter":
            num_weight=quantity.split()[0]
            price=price/num_weight
            quantity=1

        else:
            quantity=quantity
            price=price

        return price,quantity

    except:
        print("it is not possible at all")


