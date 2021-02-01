import React from 'react';
import { createStackNavigator } from 'react-navigation-stack';
import { createBottomTabNavigator } from 'react-navigation-tabs';
import HomeScreen from './src/screen/Home'
import DetailScreen from './src/screen/Detail'
import SettingScreen from './src/screen/Setting'
import SavingScreen from './src/screen/Saving'
import NotificationScreen from './src/screen/Notification'
const HomeStack = createStackNavigator({
    Home: {
        screen: HomeScreen,
    },
    Detail: {
        screen: DetailScreen
    }
});
const SettingStack = createStackNavigator({
    Setting:{
        screen: SettingScreen
    }
})
const SavingStack = createStackNavigator({
    Saving:{
        screen: SavingScreen
    }
})
const NotifiStack = createStackNavigator({
    Notification:{
        screen:NotificationScreen
    }
})
const AppNavigator = createBottomTabNavigator({
    Home: HomeStack,
    Saving: SavingStack,
    Notification:NotifiStack,
    Setting: SettingStack,
 
})
export default AppNavigator