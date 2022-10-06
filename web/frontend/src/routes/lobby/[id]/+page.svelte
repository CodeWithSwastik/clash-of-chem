<script lang="ts">
    import SmallCard from '$lib/components/SmallCard.svelte';
	import LoadingCard from '$lib/components/LoadingCard.svelte';

	import { onMount } from 'svelte';
    import io from "socket.io-client";
	import { goto } from '$app/navigation';

    export let data: {lobby: Lobby};

    type ClickCallback = () => void;

    let start: ClickCallback, leave: ClickCallback;
    let isOwner: boolean = true;
    let loaded: boolean = false;

    let players: any[] = [];
    let countdown: NodeJS.Timer;
    let countdownSeconds = 300;

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
            players = d.data.players;
            countdownSeconds = d.data.countdown;
            console.log(players);
            isOwner = (players.length) == 1;
            
            countdown = setInterval(() => {
                countdownSeconds--;

                if (countdownSeconds == 0) {
                    start();
                }
                
            }, 1000);
            setTimeout(() => {loaded = true}, 2500);
        });

        socket.on("user_join", (d) => {
            players = d.data; 
        });

        socket.on("user_leave", (d) => {
            players = d.data;
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


    $:minutesLeft = Math.floor(countdownSeconds/60);
    $:secondsLeft = Math.floor(countdownSeconds - minutesLeft * 60)

</script>

<section>
    {#if loaded}
        <div id="countdown" class="text-7xl text-text text-center my-5">{minutesLeft}:{secondsLeft<10?'0'+secondsLeft.toString():secondsLeft}</div>
        <div class="flex justify-around my-5">
            <button on:click={isOwner? start : leave} class="p-2 bg-green hover:bg-red rounded">{isOwner? "Start": "Leave"} Clash</button>
        </div>
        <div id="players" class="flex flex-wrap py-10 px-20 justify-center">
            {#each players as player}
            <div class="my-5 mx-10">
                <SmallCard username={player.username} color={player.color}/>
            </div>
            {/each}
        </div>
    {:else}
        <LoadingCard />
    {/if}
</section>