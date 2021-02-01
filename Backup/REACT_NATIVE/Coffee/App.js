import React, { Component } from 'react';
import {SafeAreaView,StyleSheet} from 'react-native'
import HeaderUI from './src/component/Header'
// import { Container, Header, Content, Button, Text } from 'native-base';
// import AppNavigator from './AppNavigator'
// import { createAppContainer } from 'react-navigation';
// const AppContainer = createAppContainer(AppNavigator)

export default class ButtonThemeExample extends Component {
  render() {
    return (
      // <AppContainer />
      <SafeAreaView style={styles.container}>
        <HeaderUI />
      </SafeAreaView>
    );
  }
}
const styles = StyleSheet.create({
  container:{
    flex:1
  }
})