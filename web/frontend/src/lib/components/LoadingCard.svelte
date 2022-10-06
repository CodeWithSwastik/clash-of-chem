<script lang="ts">
	import { onMount } from "svelte";



    let facts = [
        "About 18% of the human body is made of carbon atoms.",
        "Carbon atoms make up the backbone of many important molecules in your body - proteins, DNA, mRNA, sugars and fats.",
        "Carbon is the fourth most lavish element in the universe, fifteenth on earth and second in the human body, after oxygen.",
        "Ev­ery hy­dro­gen atom in your body is around 13.5 bil­lion years old",
        "If you mix a liter of wa­ter in a liter of ethyl al­co­hol, you get around 1.9 liters of so­lu­tion. This is because intermolecular forces between alcohol and water are strong."
    ]
    let fact = "";
    onMount(()=> fact = facts[Math.floor(Math.random()*facts.length)]);

</script>

<div class="flex items-center justify-center h-screen">
    <div class="bg-transparent text-text rounded w-[30%] shadow-2xl p-10">
            <div class="text-center text-6xl">
                <!-- TODO: Replace with benzene-->
                <i class="fa-solid fa-atom text-red animate-spin-slow" /> 

            </div>

            <div class="text-center mt-2">{fact}</div>
    </div>
</div>