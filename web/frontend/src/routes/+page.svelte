<script lang="ts">
	import { goto } from '$app/navigation';

	let username: string;

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
		<div class="bg-sky w-[40%] rounded shadow-xl p-10">

			<div class="flex">
				<input
					type="text"
					bind:value={username}
					placeholder="Enter your name"
					class="p-2 mr-2 rounded flex-grow"
				/>
				<button on:click={start} class="bg-base hover:bg-red text-white py-2 px-3 font-bold rounded">Create Lobby</button>
			</div>
			<div>
			</div>
		</div>
	</div>
</section>
