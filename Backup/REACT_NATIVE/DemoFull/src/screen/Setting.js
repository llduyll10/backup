import React from 'react';
import { View, Text } from 'react-native';

export default class HomeScreen extends React.Component {
  static navigationOptions = {
    title:'Setting'
  }
  render() {
    return (
      <View style={{ flex: 1, alignItems: 'center', justifyContent: 'center' }}>
        <Text>Setting Screen</Text>
      </View>
    );
  }
}