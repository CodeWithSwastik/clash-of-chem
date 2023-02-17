<script lang="ts">
	import { onMount } from "svelte";

    let facts = [
        "About 18% of the human body is made of carbon atoms.",
        "Carbon atoms make up the backbone of many important molecules in your body - proteins, DNA, RNA, sugars and fats.",
        "Carbon is the fourth most lavish element in the universe, fifteenth on earth and second in the human body, after oxygen.",
        "Ev­ery hy­dro­gen atom in your body is around 13.5 bil­lion years old",
        "If you mix a liter of wa­ter in a liter of ethyl al­co­hol, you only get around 1.9 liters of so­lu­tion. Magic!",
        "The word “vi­ta­min” comes from vita (life) and amine (a ni­troge­nous or­gan­ic com­pound)",
        "The human body contains enough carbon to provide 'lead' (which is really graphite) for 9,000 pencils.",
        "Hydrofluoric acid is so corrosive that it will dissolve glass. Although it is corrosive, hydrofluoric acid is considered to be a weak acid.",
        "The nineteenth-century German chemist August Kekulé claimed to have pictured the ring structure of benzene after dreaming of a snake eating its own tail.",
        "Alcohols are so less acidic that even water is more acidic than them.",
        "There are nearly 20 compounds with the formula C6H12O6, Glucose and Fructose being just a few of them.",
        "Ethanol, or ethyl alcohol, is the only type of alcohol that you can drink without seriously harming yourself, and then only if it hasn't been denatured or doesn't contain toxic impurities.",
        "TNT (Trinitrotoluene) was first prepared in 1863 by German chemist Julius Wilbrand and originally used as a yellow dye.",
        "Phenol is a normal metabolic product, excreted in quantities up to 40 mg/L in human urine.",
        "Phenol is used in molecular biology for obtaining nucleic acids (DNA, RNA) from tissues or cell culture samples.",
        "The number of organic compounds is nearly three times the number of inorganic compounds.",
        "Friedrich Wohler in 1828 synthesized urea as the first organic compound for the first time in labrotary from ammonium cyanate.",
        "Number of organic compounds outnumber inorganic compounds by nearly 10 million.",
        "Enantiomers are a type of isomer that are non-superimposable mirror images of each other, and they can have very different biological effects.",
        "Many organic compounds have distinct smells, such as the fruity smell of esters and the pungent smell of thiols.",
        "Aromatic compounds contain a special type of bonding that gives them unique properties, such as the ability to undergo substitution reactions.",
        "Organic chemistry is essential to many fields, including medicine, materials science, and energy production.",
        "Chemists continue to discover and synthesize new organic compounds with fascinating properties and potential applications.",
        "Carbon has the unique ability to form covalent bonds with up to four other atoms, giving it a versatile ability to form a wide range of organic compounds.",
        "Many organic compounds are optically active, meaning they rotate plane-polarized light, and this property can be used to determine the structure of a molecule.",
        "The Nobel Prize in Chemistry has been awarded to numerous organic chemists for their contributions to the field, including the discovery of new reactions and synthesis of important molecules.",
        "Organic chemists often use protective groups to control the reactivity of a molecule during a synthesis, allowing them to selectively modify certain parts of a molecule without affecting others.",
        "Organic chemistry plays a key role in the development of pharmaceuticals, as the properties and behavior of organic molecules can be fine-tuned to achieve specific therapeutic effects.",
        "Many organic compounds can exist in different phases or states of matter, such as liquid crystals, which have both liquid-like and crystal-like properties.",
        "Organic chemists often use spectroscopic techniques, such as infrared and nuclear magnetic resonance (NMR) spectroscopy, to study the structures and properties of molecules.",
        "The field of organic electronics is rapidly growing, with the development of organic semiconductors and organic photovoltaics for use in electronic devices.",
        "Carbon nanotubes, which are a type of organic compound, have unique mechanical, electrical, and thermal properties that make them useful in many applications, such as nanoelectronics and nanocomposites.",
        "Many organic reactions are catalyzed by enzymes, which are biological catalysts that can speed up reactions and selectively control the formation of certain products.",
        "Amines are organic compounds that contain a nitrogen atom with a lone pair of electrons, and they can be either primary, secondary, or tertiary depending on the number of carbon groups attached to the nitrogen.",
        "Aldehydes and ketones are both carbonyl compounds that contain a carbon atom double-bonded to an oxygen atom, with aldehydes having the carbonyl group at the end of a carbon chain and ketones having it in the middle.",
        "Esters are organic compounds that contain a carbonyl group bonded to an oxygen atom and another carbon atom, and they are often responsible for the fruity smells of many fruits and flowers.",
        "Carboxylic acids are organic compounds that contain a carboxyl group, which is a carbonyl group bonded to a hydroxyl group (-COOH), and they are often responsible for the sour taste of many foods.",
        "Amino acids are organic compounds that contain both an amino group (-NH2) and a carboxyl group (-COOH), and they are the building blocks of proteins.",
        "Phenols are organic compounds that contain a hydroxyl group (-OH) bonded to a benzene ring, and they have distinct acidic properties due to the stabilization of the negative charge on the oxygen atom by the aromatic ring.",
        "Alcohols are organic compounds that contain a hydroxyl group (-OH), and they can be either primary, secondary, or tertiary depending on the number of carbon groups attached to the carbon atom bonded to the hydroxyl group.",
        "Thiols are organic compounds that contain a sulfur atom bonded to a hydrogen atom (-SH), and they have distinctive pungent odors that are often described as smelling like rotten eggs.",
        "Nitriles are organic compounds that contain a carbon atom triple-bonded to a nitrogen atom, and they are often used in organic synthesis as versatile intermediates.",
        "Acid chlorides are organic compounds that contain a carbonyl group bonded to a chlorine atom (-COCl), and they are highly reactive compounds that are often used as acylating agents in organic synthesis.",
        "The word 'organic' originally referred to compounds that came from living organisms, but now refers to any compound that contains carbon.",    
        "Carbon is unique in its ability to form long chains and branched structures, which makes it the basis for the incredible diversity of organic molecules.",    
        "The chirality of a molecule refers to its 'handedness.' Chiral molecules have mirror-image isomers that are not superimposable.",    
        "Most natural amino acids, the building blocks of proteins, are chiral and exist in the L-configuration, while most sugars are chiral and exist in the D-configuration.",    
        "The smell of a molecule is often related to its shape and functional groups. For example, esters are often responsible for fruity smells, while thiols are responsible for the smell of skunks.",    
        "The discovery of the buckminsterfullerene (C60) molecule in 1985 led to the development of the field of nanotechnology.",    
        "Organic chemistry has important applications in medicine, as many drugs are organic compounds.",    
        "The polymer polyethylene is the most common plastic and is used in a wide variety of applications, including packaging and pipes.",    
        "The reactions that occur in photosynthesis, the process by which plants produce energy from sunlight, are all organic chemistry reactions.",    
        "The longest organic compound ever synthesized is a carbon chain with 200,000 atoms, known as 'tetranitratoxycarbon.'"        
    ]
    let fact = "";
    onMount(()=> fact = facts[Math.floor(Math.random()*facts.length)]);

</script>
<style lang="scss">
    @import "../../style.scss";
		.animate_in {
			@include animate_in(2);
		}
</style>
<div class="flex items-center justify-center h-screen">
    <div class="animate_in bg-mantle text-text rounded-2xl shadow-mantle w-[90%] md:w-[30%] shadow-2xl p-10">
            <div class="text-center text-6xl">
                <!-- TODO: Replace with benzene-->
                <i class="fa-solid fa-atom text-sky animate-spin-slow" /> 
            </div>

            <div class="text-center mt-2 text-text">{fact}</div>
    </div>
</div>