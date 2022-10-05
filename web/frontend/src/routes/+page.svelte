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
		<div class="bg-gray-400 h-[50%] w-[50%] rounded shadow-xl p-10">
			<div class="flex">
				<input
					type="text"
					bind:value={username}
					placeholder="Enter your name"
					class="p-2 mr-2 rounded flex-grow"
				/>
				<button on:click={start} class="bg-green-300 hover:bg-green-400 py-2 px-3 font-bold rounded">Create Lobby</button>
			</div>
			<div>
				<div class="my-10 text-2xl">Instructions to play</div>
				<div>
					<ul class="list-disc">
						<li class="my-2">
							Lorem amet consectetur adipisicing elit. Similique Dignissimos, nesciunt?
						</li>
						<li class="my-2">
							Lorem amet consectetur adipisicing elit. Similique Dignissimos, nesciunt?
						</li>
						<li class="my-2">
							Lorem amet consectetur adipisicing elit. Similique Dignissimos, nesciunt?
						</li>
					</ul>
				</div>
			</div>
		</div>
	</div>
</section>
