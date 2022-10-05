<script lang="ts">
    import SmallCard from '$lib/components/SmallCard.svelte';
	import { onMount } from 'svelte';
    import io from "socket.io-client";
	import { goto } from '$app/navigation';

    export let data: {lobby: Lobby};

    type ClickCallback = () => void;

    let start: ClickCallback, leave: ClickCallback;
    let isOwner: boolean = true;

    let players = [];

    onMount(() => {
        console.log(data);
        let username = localStorage.getItem("username");
        const socket = io("http://127.0.0.1:8000", {
            auth: {
                username: username,
                room: data.lobby.id
            }
        });
        socket.on("connect", () => console.log("connected"));
        socket.on("room_details", (d) => {
            players = d.data;
            isOwner = (players.length) == 1;
        });

        socket.on("user_join", (d) => {
            if (d.data != username) {
                players = [...players, d.data];
            }
        });

        start = () => {
            clearInterval(countdown);
        };

        leave = () => {
            socket.disconnect();
            goto('/');
        }

    });

    interface Lobby {
        id: string,
    }


    let countdownSeconds = 300;
    $:minutesLeft = Math.floor(countdownSeconds/60);
    $:secondsLeft = Math.floor(countdownSeconds - minutesLeft * 60)
    const countdown = setInterval(() => {
        countdownSeconds--;

        if (countdownSeconds == 0) {
            start();
        }
    }, 1000);
</script>

<section>
    <div id="countdown" class="text-7xl text-gray-300 text-center my-5">{minutesLeft}:{secondsLeft<10?'0'+secondsLeft.toString():secondsLeft}</div>
    <div class="flex justify-around my-5">
        <button on:click={isOwner? start : leave} class="p-2 bg-green-400 hover:bg-green-500 rounded">{isOwner? "Start": "Leave"} Clash</button>
    </div>
    <div id="players" class="flex flex-wrap py-10 px-20 justify-center">
        {#each players as player}
        <div class="my-5 mx-10">
            <SmallCard username={player} />
        </div>
        {/each}
    </div>
</section>