<script>
// @ts-nocheck
	import SmilesDrawer from 'smiles-drawer';
	import { onMount } from 'svelte';

	let smilesDrawer = new SmilesDrawer.Drawer({});
	let pfpColors = ['mauve', 'red', 'peach', 'green', 'sky', 'blue'];
	let randomPfpColor = () => {
		return pfpColors[Math.floor(Math.random() * pfpColors.length)]
	};

	//c1Nc(F)c=c(Br)c(Cl)c1c(=O)cO
	onMount(() => {
		SmilesDrawer.apply({
			width: 200,
			height: 200,
			themes: {
			dark: {
				C: '#cdd6f4',
				O: '#f38ba8',
				N: '#89b4fa',
				F: '#94e2d5',
				CL: '#a6e3a1',
				BR: '#fab387',
				I: '#cba6f7',
				P: '#eba0ac',
				S: '#f1c40f',
				B: '#e67e22',
				SI: '#e67e22',
				H: '#f2cdcd',
				BACKGROUND: '#1e1e2e'
			},
		},
		}, 'canvas[data-smiles]', 'dark', null);
	});
	

	export let data;
	let numPlayers = data.numPlayers ?? 6;
	console.log(data.id);
</script>

<section class="flex">
	<div id="players" class="flex flex-col overflow-scroll w-[30%] h-screen border-r border-surface1">
		<div class="px-5 pt-5 text-center text-2xl text-text">Challenge 1</div>
		<div class="text-center text-text mb-5">{numPlayers} Players</div>
		{#each Array(6) as _, i}
			<div class="p-4 flex {i%2===0?'bg-surface0':''}">
				<i class="fa-solid fa-user p-1 mr-2 bg-peach text-mantle rounded"/> 
				<div class="text-text">{'midnight'}</div>
				<div class="flex-grow"></div>
				<div class="text-text font-bold">{'18'} points</div>
			</div>
		{/each}
	</div>
	<div id="content" class="flex flex-col w-[70%]">
		<div id="stats" class="flex p-2 border-b border-surface1">
			<div class="flex-grow"></div>
			<div class="text-text text-xl"><span>{'18 points'}</span> | <span class="">{'5:00'}</span></div>
		</div>
		<div class="flex justify-center pt-10">
			<canvas data-smiles="CC=1C([N+](=O)[O-])=CC([N+](=O)[O-])=CC1[N+](=O)[O-]"/>
			<div class="w-[200px]"></div>
			<canvas data-smiles="cc(Br)cc"></canvas>
		</div>
	</div>
</section>