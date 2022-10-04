<script lang="ts">
	let text = "";
</script>

<svelte:head>
	<title>Home</title>
	<meta name="description" content="Clash of Chem" />
</svelte:head>

<div class="text-white bg-gray-900 rounded block m-auto max-w-lg p-8 mt-6">
	<h1 class="text-6xl text-bold pl-6 pb-8 pr-8">
		Clash of Chem
	</h1>

	<div>
		<input bind:value={text} class="bg-gray-700 rounded p-2 w-full mb-4" placeholder="Enter your name">
		<button class="text-white bg-blue-700 mr-2 hover:bg-blue-800 focus:ring-4 focus:ring-blue-300 font-medium rounded-lg text-sm px-5 py-2.5 dark:bg-blue-600 dark:hover:bg-blue-700 focus:outline-none dark:focus:ring-blue-800">Create Lobby</button>
	</div>
</div>