<script lang="ts">
	import { onMount } from "svelte";

    let facts = [
        "About 18% of the human body is made of carbon atoms.",
        "Carbon atoms make up the backbone of many important molecules in your body - proteins, DNA, mRNA, sugars and fats.",
        "Carbon is the fourth most lavish element in the universe, fifteenth on earth and second in the human body, after oxygen.",
        "Ev­ery hy­dro­gen atom in your body is around 13.5 bil­lion years old",
        "If you mix a liter of wa­ter in a liter of ethyl al­co­hol, you only get around 1.9 liters of so­lu­tion. Magic!",
        "The word “vi­ta­min” comes from vita (life) and amine (a ni­troge­nous or­gan­ic com­pound)"
    ]
    let fact = "";
    onMount(()=> fact = facts[Math.floor(Math.random()*facts.length)]);

</script>
<style lang="scss">
    @import "../../style.scss";
		// .animate_out {
		// 	@include animate_out(2);
		// }
		.animate_in {
			@include animate_in(2);
		}
</style>
<div class="flex items-center justify-center h-screen">
    <div class="animate_in bg-mantle text-text rounded-2xl shadow-mantle w-[30%] shadow-2xl p-10">
            <div class="text-center text-6xl">
                <!-- TODO: Replace with benzene-->
                <i class="fa-solid fa-atom text-sky animate-spin-slow" /> 
            </div>

            <div class="text-center mt-2 text-text">{fact}</div>
    </div>
</div>