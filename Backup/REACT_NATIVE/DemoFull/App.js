import React, { Component } from 'react';
import { Container, Header, Content, Button, Text } from 'native-base';
import AppNavigator from './AppNavigator'
import { createAppContainer } from 'react-navigation';
const AppContainer = createAppContainer(AppNavigator)
export default class ButtonThemeExample extends Component {
  render() {
    return (
      <AppContainer />
    );
  }
}