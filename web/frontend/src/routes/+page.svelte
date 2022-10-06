<script lang="ts">
	import { goto } from '$app/navigation';
	import { onMount } from 'svelte';

	let username: string = "";

	onMount(() => {
		username = localStorage.getItem('username') ?? '';
	})

	let start = () => {
		localStorage.setItem('username', username);
		goto('/lobby/test');
	};
</script>

<svelte:head>
	<title>Home</title>
	<meta name="description" content="Clash of Chem" />
</svelte:head>

<section>
	<div class="flex items-center justify-center h-screen">
		<div class="bg-mantle rounded w-[30%] shadow-xl p-10">

			<div>
				<input
					type="text"
					bind:value={username}
					placeholder="Enter your name"
					class="p-2 mr-2 rounded w-full bg-surface1 text-text"
				/>
			</div>
			<div>
			<button on:click={start} class="bg-green hover:bg-opacity-70 text-base hover:text-black py-2 px-3 mt-8 w-full font-bold rounded">Play!</button>
				</div>
			<div>
				<button on:click={start} class="bg-sapphire hover:bg-opacity-70 text-base hover:text-black py-2 px-3 mt-2 w-full font-bold rounded">Create Private Lobby</button>
			</div>

			<div>
			</div>
		</div>
	</div>
</section>
