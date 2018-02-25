# Change Log
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](http://keepachangelog.com/)
and this project adheres to [Semantic Versioning](http://semver.org/).

## [Unreleased]
### changed
- Fix: Removes call to method _get_delivery_methods() original.
- Fix: iteare only over factible carriers
- Fix: no returns carriers if shipping address has no zip code.

## [9.0.1.0.2] 2018-02-13
### changed
- Fix: Calls to method _get_delivery_carrier_id() passing the available carriers ids.

## [9.0.1.0.1] 2018-02-09
### changed
- Fix: Calls method _get_delivery_carrier_id() in sale with parameter website enabled.

## [9.0.1.0.0] - 2018-02-09
### added
- Autodetects delivery method in ecommerce
