<template>
  <v-container style="height:100%">
    <v-row>
      <v-col cols="4">
        <v-row>
          <v-card>
            <v-card-title class="justify-center">Query</v-card-title>
            <v-tabs
                background-color="deep-purple accent-4"
                grow
                dark
            >
              <v-tab key="tab1">Samples</v-tab>
              <v-tab-item key="tab1">
                <v-card height="200pt" width="300pt">

                  <v-container fluid>
                    <v-combobox
                        v-model="query_datasets"
                        :items="datasets"
                        hide-selected
                        hint="Maximum of 5 tags"
                        label="Add some tags"
                        multiple
                        small-chips
                        solo
                        deletable-chips
                        hide-details
                    >

<!--                      <template v-slot:selection="{ item }">-->
<!--                        <v-chip :color="randomColor(item)" class="v-chip&#45;&#45;removable">-->
<!--                      <span class="pr-2">-->
<!--                                                {{ item }}-->
<!--                      </span>-->
<!--                        </v-chip>-->
<!--                      </template>-->

                      <template v-slot:item="{ item }">
                        <v-chip :color="randomColor(item)">{{ item }}</v-chip>
                      </template>
                    </v-combobox>
                  </v-container>

                  <v-virtual-scroll
                      height="180"
                      item-height="60"
                      :items="sampleRows"
                  >
                    <template v-slot:default="{ item }">
                      <v-list-item :key="item">
                        <v-list-item-content>
                          <v-row>
                            <v-col
                                v-for="it in item"
                                :key="it"
                            >
                              <v-img
                                  :lazy-src="`https://picsum.photos/10/6?image=${it}`"
                                  height="40"
                                  width="40"
                                  :src="`https://picsum.photos/500/300?image=${it}`"
                                  @click="chooseClick(it)"
                              ></v-img>
                            </v-col>
                          </v-row>
                        </v-list-item-content>
                      </v-list-item>
                    </template>
                    <v-divider></v-divider>

                  </v-virtual-scroll>
                </v-card>
              </v-tab-item>
              <v-tab key="tab2">Upload</v-tab>
              <v-tab-item key="tab2">
                <v-card height="200pt" width="300pt" style="display:flex;justify-content:center;align-items:center">
                  <v-btn
                      depressed
                      color="primary"
                  >
                    Upload File
                  </v-btn>
                </v-card>
              </v-tab-item>
            </v-tabs>
          </v-card>
        </v-row>

        <v-row>
        </v-row>
      </v-col>

      <v-col cols="8">
        <v-card>


        </v-card>
      </v-col>
    </v-row>
  </v-container>


</template>

<script>
export default {
  name: "Page",
  data() {
    return {
      datasets: ['Dataset1', 'Dataset2', 'Dataset3', 'Dataset4', 'Dataset5', 'Dataset6'],
      sampleRows: [
        ['1', '2', '3', '4', '5'],
        ['1', '2', '3', '4', '5'],
        ['1', '2', '3', '4', '5'],
        ['1', '2', '3', '4', '5'],
        ['1', '2', '3', '4', '5'],
        ['1', '2', '3', '4', '5'],
        ['1', '2', '3', '4', '5'],
      ]
    }
  },
  methods: {
    chooseClick(index) {
      console.log(index)
    },
    randomColor(s) {
      if (s === "Dataset1") {
        return "blue"
      } else {
        return "red"
      }
    }
  }
}
</script>

<style scoped>

</style>