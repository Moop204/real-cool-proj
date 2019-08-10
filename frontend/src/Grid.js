import React from 'react'
import WebMap from './Map'
import Detail from './Detail'
import { Grid, Image } from 'semantic-ui-react'

const GridExampleColumnWidth = () => (
  <Grid>
    <Grid.Column width={12}>
      <WebMap />
    </Grid.Column>
    <Grid.Column width={2}>
      <Detail />
    </Grid.Column>
  </Grid>
)

export default GridExampleColumnWidth

