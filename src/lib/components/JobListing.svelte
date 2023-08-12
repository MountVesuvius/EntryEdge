<script>
    import Chip from "./Chip.svelte";

    export let color = "#DAF5ED";
    export let company = "Amazon";
    export let title = "Senior UI/UX Designer";
    export let jobLink = "https://www.seek.com.au/";
    export let description = "Nisi laboris qui laborum sunt irure veniam eiusmod officia do quis exercitation aliqua. Nisi laboris qui laborum sunt irure veniam ";
    // export let area = "Computer Science";
    export let companyImg = "https://assets.aboutamazon.com/dims4/default/47b2485/2147483647/strip/true/crop/198x73+0+0/resize/300x111!/quality/90/?url=https%3A%2F%2Famazon-blogs-brightspot.s3.amazonaws.com%2Fd7%2F46%2F57d4c6d54c5bafd771a85f5058fe%2Ffire-tablet-0.jpg";
</script>

<div class="bg-white my-3 sm:m-3 rounded-xl p-3 sm:w-96" style="font-family: 'Nunito';">
    <section class="p-3 rounded-xl h-80 flex flex-col justify-start" style="background-color: {color}">
        <div class="flex">
            <div class="w-72">
                <span class="font-bold ">{company}</span>
                <h2 class="font-extrabold text-2xl">{title}</h2>
            </div>
            <div class="w-8 h-8 rounded-full bg-white flex items-center justify-center"><img src="icons/bookmark.svg" alt="bookmark" class=""></div>
        </div>
        <p class="w-80 overflow-ellipsis">{description}</p>
        <!-- <div> -->
            <!-- <Chip content={area}/> -->
        <!-- </div> -->
    </section>

    <div class="flex justify-between items-center mr-4 mt-2">
        <img src={companyImg} alt="company logo" class="object-contain h-20 w-24 justify-self-start">
        <a href={jobLink}><button class="bg-black text-white px-6 py-4 rounded-full">Details</button></a>
    </div>
</div>
