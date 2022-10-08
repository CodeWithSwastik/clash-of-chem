<script lang="ts">
    // @ts-nocheck
    import SmallCard from '$lib/components/SmallCard.svelte';
	import LoadingCard from '$lib/components/LoadingCard.svelte';
    import { socket } from "$lib/stores/socket.js";

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
        let username = localStorage.getItem("username");
        if ($socket) {
            loaded = true;
        }
        else {
            const socketConnection = io("http://127.0.0.1:8000", {
                auth: {
                    username: username,
                    room: data.lobby.id
                }
            });
            socket.set(socketConnection);
        $socket.on("connect", () => {
            console.log("connected");
        });

        
        $socket.on("room_details", (d) => {
            players = d.data.players;
            countdownSeconds = d.data.countdown;
            isOwner = d.data.owner == username;
            
            countdown = setInterval(() => {
                countdownSeconds--;

                if (countdownSeconds == 0) {
                    start();
                }
                
            }, 1000);
            setTimeout(() => {loaded = true}, 2500);
        });

        $socket.on("user_join", (d) => {
            players = d.data; 
        });

        $socket.on("user_leave", (d) => {
            players = d.data;
        });

        $socket.on("clash_started", (d) => {
            console.log("Starting");
            goto("/clash/"+data.lobby.id);
        });

        start = () => {
            clearInterval(countdown);


            if (isOwner && $socket) {
                console.log("starting?");
                $socket.emit("start_clash", {"room": data.lobby.id});
            }
        };

        leave = () => {
            $socket.disconnect();
            goto('/');
        }
        }

    });

    interface Lobby {
        id: string,
    }


    $:minutesLeft = Math.floor(countdownSeconds/60);
    $:secondsLeft = Math.floor(countdownSeconds - minutesLeft * 60)

    let anim_delay = 0;
    let get_delay = () => {
        anim_delay += 1;
        return anim_delay
    };

</script>
<style>
    @keyframes popin {
    0% {
        opacity: 0;
        scale: 0%;
    }
    100% {
        opacity: 1;
        scale: 100%;
    } 
}
    .pop_in{
        animation: popin 0.3s ease-in-out;
        animation-fill-mode: forwards;
    }
</style>
<section>
    {#if loaded}
        <div id="countdown" class="text-7xl text-text text-center my-5">{minutesLeft}:{secondsLeft<10?'0'+secondsLeft.toString():secondsLeft}</div>
        <div class="flex justify-around my-5">
            <button on:click={isOwner? start : leave} class="p-2 bg-green hover:bg-red rounded">{isOwner? "Start": "Leave"} Clash</button>
        </div>
        <div id="players" class="flex flex-wrap py-10 px-20 justify-center">
            {#each players as player}
            <div class="pop_in my-5 mx-10 animate_in">
                <SmallCard username={player.username} color={player.color}/>
            </div>
            {/each}
        </div>
    {:else}
        <LoadingCard/>
    {/if}
</section>