<script lang="ts">
	import { goto } from '$app/navigation';
	import { onMount } from 'svelte';

	let username: string = "";
	let lobby: string = "";


	onMount(() => {
		username = localStorage.getItem('username') ?? '';
	})

	let animateOut = false;
	let start = () => {
		if (username.length > 24 || username.length < 2)
			return alert('Username must be between 2-24 chars (inclusive).');
		localStorage.setItem('username', username);
		animateOut = true;
		setTimeout(() => {
			let r = Math.random().toString(36).slice(2, 7);
			goto('/lobby/' + (lobby ? lobby : r));
		}, 700)
	};
</script>

<svelte:head>
	<title>Home</title>

	<style lang="scss">		
		@import "../style.scss";

		.animate_out {
			@include animate_out(3);
		}
	</style>
</svelte:head>

<section>
	<div class="flex items-center justify-center h-screen z-10">
		<div class="bg-mantle rounded-2xl min-w-[30%] shadow-2xl shadow-mantle p-10 {animateOut? 'animate_out': ''}">
 
			<div>
				<input
					type="text"
					bind:value={username}
					placeholder="Enter your name"
					class="p-2 mr-2 rounded-xl w-full bg-surface1 text-text"
				/>
			</div>

			<div class="grid grid-cols-2 mt-10">
				<input
					type="text"
					bind:value={lobby}
					placeholder="Enter lobby code"
					class="p-2 mr-2 rounded-xl bg-surface1 text-text"
				/>
				<button on:click={start} class="bg-green hover:bg-opacity-70 text-base hover:text-black py-2 px-3 font-bold rounded-xl">Play!</button>
			</div>
			<div>
				<button on:click={start} class="bg-sapphire hover:bg-opacity-70 text-base hover:text-black py-2 px-3 mt-5 w-full font-bold rounded-xl">Create Private Lobby</button>
			</div>
		</div>
	</div>
</section>
