<script>
// @ts-nocheck
	import SmilesDrawer from 'smiles-drawer';
	import { onMount } from 'svelte';
	import { socket } from '$lib/stores/socket.js';
	import LoadingCard from '$lib/components/LoadingCard.svelte';
	import { goto } from '$app/navigation';
    import io from "socket.io-client";
    import { PUBLIC_API_URL } from "$env/static/public";

	let smilesDrawer = new SmilesDrawer.Drawer({
			width: 250,
			height: 250,
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


	let loaded = false;
	let username = "";
	let winner = null;
	let menuOpen = false;

	let leaderboard = {
		"Mid":10,
		"Swas": 69
	};
	let challenge = {
		number: 1,
		type: "strategy",
		time: 60,
		current: "C",
		turn: "Swas",
		targets: {
			"Swas": "1-Chloropropane",
		},
		reagents: [],
		viewers: 0,
	};

	let challengeNumber = 1;
	let challengeLoaded = false;

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
		'lavender': "#b4befe",
		'red': "#f38ba8",
		'green': "#a6e3a1",
		'mantle': "#181825",
		'crust': "#11111b",
		'text': "#cdd6f4",
    };

	let viewerMode = false;
	let viewerCount = 0;
	//c1Nc(F)c=c(Br)c(Cl)c1c(=O)cO
	onMount(() => {
        username = localStorage.getItem("username");
        if (!username) {
            username = "User#" + Math.floor(Math.random()*9000 + 1000);
            localStorage.setItem("username", username);
        }

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
			$socket.emit("request_clash_details", {
				"clash": data.id,
			}, (d) => {
				if (d=="Viewer") {
					viewerMode = true;
				} else if (d == "Invalid") {
					goto("/");
				}
			});

			$socket.on("clash_details", (d) => {
				leaderboard = d.data.leaderboard;
				numPlayers = Object.keys(leaderboard).length;
				players = d.data.players;
				viewerCount = d.data.viewers;
				console.log(d.data);

				if (!loaded) {
				setInterval(
					()=>{challenge.time--;}, 1000
				);
				loaded = true;
				}
			});
			$socket.on("conversion", (d) => {
				console.log(d);
			}
			});
			$socket.on("new_challenge", (d) => {
				challengeLoaded = true;
				console.log(d);
				challenge = d.data;
				challengeNumber ??= challenge.number;
				if (challenge.type == "conversion") {
					chosenAnswer = null;
					answerResult = null;
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
				} else {
					SmilesDrawer.parse(challenge.current, function (tree) {
						smilesDrawer.draw(tree, 'current-compound-canvas', 'dark', false);
					}, function (err) {
						console.log(err);
					});					
				}
			});
			$socket.on("clash_over", (d) => {
				console.log("GG! Clash is over");
				winner = d.data;
				setTimeout(() => {goto("/")}, 10000);
			});

		}
		else {
            goto("/lobby/"+data.id);
		}
	});
	
	let chosenAnswer = null;
	let answerResult = null;

	const getStylesForButton = (reagent) => {
		if (chosenAnswer == reagent) {
			let bg = answerResult == "wrong" ? colors.red : colors.green;
			return "background-color:" + bg + "; color: " + colors.crust;
		} 
		return "background-color:" + colors.crust + "; color: " + colors.text;
	}
	const answer = (ans) => {
		chosenAnswer = ans;
		$socket.emit("clash_answer", {"clash": data.id, "answer": ans}, (res) => {
			answerResult = res ? "correct" : "wrong"
		});
	}

	const strategy_update = (reagent) => {
		$socket.emit("clash_strategy_update", {"clash": data.id, "reagent": reagent});
	}

	export let data;
	let numPlayers = data.numPlayers ?? 2;
	console.log(data.id);


</script>
{#if loaded}
<section class="flex">
	<div id="players" class="hidden md:flex flex-col w-[30%] h-screen border-r border-surface1">
		<div class="px-5 pt-5 text-center text-2xl text-text">Challenge {challengeNumber}</div>
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
	<div id="players" class="absolute {menuOpen?'flex':'hidden'} w-[80%] bg-crust md:hidden flex-col overflow-scroll h-screen border-r border-surface1">
		<button class="text-text p-2 m-2 rounded bg-crust" on:click={() => {menuOpen=false}}><i class="fa-solid fa-arrow-left"></i></button>
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
	<div id="content" class="flex flex-col md:w-[70%]">
		<div id="stats" class="flex p-2 border-b border-surface1">
			<button class="md:hidden text-text" on:click={() => {menuOpen = true}}><i class="fa-solid fa-bars"></i></button>
			<div class="flex-grow"></div>
			<div class="text-text text-xl">
				{#if leaderboard[username]}
				<span>{leaderboard[username]} points</span> | 
				{/if}
				{#if viewerCount}
				<i class="fa-solid fa-eye" /> <span class="">{viewerCount} </span> |
				{/if}
				<i class="fa-solid fa-clock" /> <span class="">{challenge.time}</span>
			</div>
		</div>
		{#if winner}
			<div class="text-text text-4xl text-center pt-10">GG! The Clash is over! The winner is {winner}</div>
		{:else}
			{#if challenge.type == 'conversion'}	
				<div class="flex justify-center pt-10">
					<canvas id="from-compound-canvas" data-smiles="C"/>
					<div class="w-[200px] text-text text-4xl text-center flex h-full"><div class="m-auto">to</div></div>
					<canvas id="to-compound-canvas" data-smiles="F"></canvas>
				</div>
				{#if challengeLoaded}
				<div class="pt-10">
					<div class="text-text m-4 mb-8 text-4xl"> Which reagent will carry out the conversion? </div>
					<div class="grid grid-cols-2 gap-4 m-4 {answerResult ? 'pointer-events-none': ''}">
					{#each challenge.reagents as reagent}
							<button on:click={() => answer(reagent)} class="text-text bg-crust rounded p-3 hover:bg-mantle" style={getStylesForButton(reagent)}>{reagent}</button>
					{/each}
					</div>
				</div>
				{/if}
			{:else}
				<div class="flex justify-center pt-10">
					<canvas id="current-compound-canvas" data-smiles="C"/>
				</div>
				{#if challenge.winner}
					<div class="text-text m-4 text-4xl"> {challenge.winner} has won this challenge! </div>

				{:else}
				{#if challengeLoaded}
					<div class="pt-10">
						<div class="text-text m-4 text-4xl"> {challenge.turn == username ? 'Which reagent will you use?' : `Waiting for ${challenge.turn} to select a reagent...`} </div>
						<div class="text-overlay2 m-4 text-2xl"> Current turn: {challenge.turn} </div>
						{#if !viewerMode} 
							<div class="text-overlay2 m-4 mt-2 text-2xl"> Your goal: Convert to {challenge.targets[username]} </div>
						{/if}

						<div class="grid grid-cols-2 gap-4 m-4 {challenge.turn != username ? 'pointer-events-none': ''}">
						{#each challenge.reagents as reagent}
								<button on:click={() => strategy_update(reagent)} class="text-text bg-crust rounded p-3 hover:bg-mantle">{reagent}</button>
						{/each}
						</div>
					</div>
				{/if}			
				{/if}	
			{/if}
		{/if}
	</div>
</section>
{:else}
<LoadingCard />
{/if}