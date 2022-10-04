<script lang="ts">
    import SmallCard from '$lib/components/SmallCard.svelte';

    interface Lobby {
        id: string,
    }

    export let data: {lobby: Lobby};

    let countdownSeconds = 300;
    $:minutesLeft = Math.floor(countdownSeconds/60);
    $:secondsLeft = Math.floor(countdownSeconds - minutesLeft * 60)
    const countdown = setInterval(() => {
        countdownSeconds--;

        if (countdownSeconds == 0) {
            start();
        }
    }, 1000);

    let start = () => {
        clearInterval(countdown);
    };
</script>

<section>
    <div id="countdown" class="text-7xl text-gray-300 text-center my-5">{minutesLeft}:{secondsLeft<10?'0'+secondsLeft.toString():secondsLeft}</div>
    <div class="flex justify-around my-5">
        <button on:click={start} class="p-2 bg-green-400 hover:bg-green-500 rounded">Start Clash</button>
    </div>
    <div id="players" class="flex flex-wrap py-10 px-20 justify-around">
        {#each Array(11) as _, i}
        <div class="my-5 mx-3">
            <SmallCard username={"midnight"} />
        </div>
        {/each}
    </div>
</section>