<script>
    // import Posting from "$lib/components/Posting.svelte";
    import JobListing from '$lib/components/JobListing.svelte';
    import jobs from '$lib/data/output.json';

    const colors = [
        "#FFE1CC", 
        "#FFD1E8", 
        "#E1FFD1", 
        "#CCF5FF", 
        "#FFCCF2", 
        "#F2DFFF", 
        "#E0E4FF", 
        "#D5FFFB", 
        "#FFFAE1", 
    ]
    let selectedColor = colors[6];
    let isJobTypeOpen = false;
    let selectedJobs = jobs.Accounting;
    let jobArea = 'Accounting';

    function selectJob(job, area) {
        selectedJobs = job;
        // selectedColor = pickRandomColor();
        jobArea = area;
    }

    function pickRandomColor() {
        let picked = colors[Math.floor(Math.random() * colors.length)];
        // colors.splice(colors.indexOf(picked), 1);
        return picked;
    }
</script>

<div class="w-screen flex flex-col items-center justify-center text-center text-white mb-6">
    <h1 class="text-[1.5rem] sm:text-[4rem] font-bold typed">Find Your First Student Job</h1>
    <h3 class="sm:text-[2rem]">Launching your careers, the right way</h3>
</div>


<div class="flex flex-col justify-center sm:ml-[8%]">
    <button on:click={() => {isJobTypeOpen = !isJobTypeOpen;}} class="text-white bg-blue-600 w-60 flex items-center justify-center py-2 rounded-md">
        Job Type
        <svg class="w-2.5 h-2.5 ml-2.5" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 10 6">
            <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="m1 1 4 4 4-4"/>
        </svg>
    </button>
    <!-- Dropdown menu -->
    {#if isJobTypeOpen}
    <div id="dropdown" class="z-10 bg-white divide-y divide-gray-100 rounded-lg shadow w-60 dark:bg-gray-700">
        <ul class="py-2 text-sm text-gray-700 h-48 overflow-y-auto space-y-1">
            {#each Object.keys(jobs) as item}
                <button class="text-white text-start text-lg w-60 px-2 focus:bg-white focus:text-black" on:click={() => {selectJob(jobs[item], item)}}>{item}</button>
            {/each}
        </ul>
    </div>
    {/if}
</div>

<div class="flex flex-col flex-wrap sm:flex-row justify-center">
    {#each selectedJobs as job}
        <JobListing 
            title={job.title}
            companyImg={job.companyImg}
            company={job.company}
            jobLink={job.jobLink}
            description={job.description}
            area={jobArea}
            color={selectedColor}
        />
    {/each} 
</div>


<style>
.typed {
  overflow: hidden;
  white-space: nowrap;
  border-right: 2px solid;
  width: 0;
  animation: typing 2s steps(40, end) forwards, blinking 1s 2s;
}
  
@keyframes typing {
  from { width: 0; border-color: white; }
  40% {border-color: transparent}
  to { width: 102%; border-color: transparent }
}

@keyframes blinking {
  0% {border-color: transparent}
  40% {border-color: white}
  100% {border-color: transparent}
}

</style>