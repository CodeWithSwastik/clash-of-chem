<script>
// @ts-nocheck
	import SmilesDrawer from 'smiles-drawer';
	import { onMount } from 'svelte';
	import { socket } from '$lib/stores/socket.js';
	import LoadingCard from '$lib/components/LoadingCard.svelte';

	let smilesDrawer = new SmilesDrawer.Drawer({
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
				}
			}
		}	
		);

	let pfpColors = ['mauve', 'red', 'peach', 'green', 'sky', 'blue'];
	let randomPfpColor = () => {
		return pfpColors[Math.floor(Math.random() * pfpColors.length)]
	};

	let loaded = false;

	let leaderboard = {
		"Mid":10,
		"Swas": 69
	};
	let challenge = {
		number: 1,
		time: 60,
		from: "C",
		to: "CC",
		reagents: [],
	}

	let players = {
		"Mid": {
			"color": "rosewater",
		},
		"Swas": {
			"color": "sky",
		},
	};

	let colors = {
		'rosewater': "#f5e0dc",
		'pink': "#f5c2e7", 
		'maroon': "#eba0ac", 
		'peach': "#fab387", 
		'yellow': "#f9e2af", 
		'teal': "#94e2d5", 
		'sky': "#89dceb", 
		'lavender': "#b4befe"
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

		if ($socket) {
			$socket.on("clash_details", (d) => {
				leaderboard = d.data.leaderboard;
				numPlayers = Object.keys(leaderboard).length;
				players = d.data.players;
				console.log(players);
				loaded = true;
			});
			$socket.on("new_challenge", (d) => {
				console.log(d);
				challenge = d.data;
				SmilesDrawer.parse(challenge.from, function (tree) {
					smilesDrawer.draw(tree, 'from-compound-canvas', 'dark', false);
				}, function (err) {
					console.log(err);
				});

				SmilesDrawer.parse(challenge.to, function (tree) {
					smilesDrawer.draw(tree, 'to-compound-canvas', 'dark', false);
				}, function (err) {
					console.log(err);
				});
			});
		}
	});
	

	export let data;
	let numPlayers = data.numPlayers ?? 2;
	console.log(data.id);
</script>
{#if loaded}
<section class="flex">
	<div id="players" class="flex flex-col overflow-scroll w-[30%] h-screen border-r border-surface1">
		<div class="px-5 pt-5 text-center text-2xl text-text">Challenge {challenge.number}</div>
		<div class="text-center text-text mb-5">{numPlayers} Players</div>
		{#each Object.entries(leaderboard) as [player, points], i}
			<div class="p-4 flex {i%2===0?'bg-surface0':''}">
				<i class="fa-solid fa-user p-1 mr-2 text-mantle rounded" style="background-color: {colors[players[player].color]}"/> 
				<div class="text-text">{player}</div>
				<div class="flex-grow"></div>
				<div class="text-text font-bold">{points} points</div>
			</div>
		{/each}
	</div>
	<div id="content" class="flex flex-col w-[70%]">
		<div id="stats" class="flex p-2 border-b border-surface1">
			<div class="flex-grow"></div>
			<div class="text-text text-xl"><span>{'18 points'}</span> | <span class="">{'5:00'}</span></div>
		</div>
		<div class="flex justify-center pt-10">
			<canvas id="from-compound-canvas"/>
			<div class="w-[200px]"></div>
			<canvas id="to-compound-canvas"></canvas>
		</div>
	</div>
</section>
{:else}
<LoadingCard />
{/if}