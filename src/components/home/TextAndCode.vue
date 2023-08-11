<template>
  <div class="relative">
    <div class="w-full max-w-6xl px-4 mx-auto">
      <div class="flex flex-wrap justify-center -mx-4 lg:justify-between">
        <div class="w-full px-4 mb-20 text-center lg:w-5/12 lg:text-left lg:mb-0">
          <h3 class="mb-4 text-4xl font-bold text-black">
            Extract, Load and Run <span class="brackets brackets-pink">With Meltano</span>
          </h3>
          <p
            class="my-8 leading-relaxed tracking-normal opacity-75 text-black/75 text-md font-grotesk lg:pr-10"
          >
            Meltano unlocks software development workflows for data movement and gives data
            engineers complete control and visibility of their pipelines, delivering unparalleled
            efficiency and confidence in every change.
          </p>
          <!-- Add URL -->
          <a
            href="#"
            class="bg-blue inline-block font-ibm text-white items-center w-auto rounded-md px-4 py-2.5 border border-blue leading-tight hover:bg-purple hover:border-purple"
            >Explore Meltano</a
          >
        </div>
        <div class="w-full max-w-2xl px-4 lg:w-7/12">
          <div
            class="relative text-sm font-normal text-white border rounded-md bg-purple font-ibm border-black/15"
          >
            <div class="absolute right-0 w-1/3 -top-1/3 lg:-top-1/2 lg:w-1/3">
              <img src="@/assets/images/meltano-d.svg" alt="Meltano" class="lg:animate-fly" />
            </div>
            <div class="flex flex-row items-center justify-between px-4 py-3">
              <div class="flex flex-row">
                <div class="w-3 h-3 mx-1 border rounded-full bg-white/5 border-white/20"></div>
                <div class="w-3 h-3 mx-1 border rounded-full bg-white/5 border-white/20"></div>
                <div class="w-3 h-3 mx-1 border rounded-full bg-white/5 border-white/20"></div>
              </div>
              <div class="tracking-widest text-white/25">Terminal</div>
              <div class="flex justify-end w-16">
                <div class="w-3 h-3 border rounded-full bg-white/5 border-white/20"></div>
              </div>
            </div>
            <div class="px-8 py-6 space-y-6 leading-relaxed border-t opacity-90 border-white/20">
              <p class="mb-6">
                meltano add extractor tap-postgres <br />
                meltano add loader target-snowflake
              </p>
              <p class="mb-6">
                cookiecutter https://github.com/meltano/sdk \ <br />
                <span class="text-green">--directory=</span>"cookiecutter/tap-template" <br />
                <span class="text-grey-medium"># source_name: my-api</span> <br />
                meltano add <span class="text-green">--custom</span> extractor tap-my-api
              </p>
              <p class="mb-6">
                meltano add transformer dbt <br />
                meltano add <span class="text-green">--custom</span> utility my-script.py
              </p>
              <p class="">
                meltano run tap-postgres target-snowflake dbt <br />
                meltano run tap-my-api target-snowflake my-script.py
              </p>
            </div>
          </div>
        </div>
      </div>
    </div>
    <div
      class="absolute w-72 h-72 top-20 bg-gradient-to-b from-pink via-purple to-blue rounded-full filter blur-[150px] opacity-50 right-0"
    ></div>
  </div>
</template>
