# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: degiro_connector/trading/models/trading_relay.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from degiro_connector.trading.models import trading_pb2 as degiro__connector_dot_trading_dot_models_dot_trading__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n3degiro_connector/trading/models/trading_relay.proto\x12\x1e\x64\x65giro_connector.trading_relay\x1a\x1cgoogle/protobuf/struct.proto\x1a\x1egoogle/protobuf/wrappers.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a-degiro_connector/trading/models/trading.proto\"]\n\tSetConfig\x12:\n\x0b\x63redentials\x18\x01 \x01(\x0b\x32%.degiro_connector.trading.Credentials\x12\x14\n\x0c\x61uto_connect\x18\x02 \x01(\x08\"u\n\x0c\x43onfirmOrder\x12\x35\n\x0f\x63onfirmation_id\x18\x01 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12.\n\x05order\x18\x02 \x01(\x0b\x32\x1f.degiro_connector.trading.Order\"\xb3\x05\n\rProductSearch\x12\x45\n\x05\x62onds\x18\x01 \x01(\x0b\x32\x34.degiro_connector.trading.ProductSearch.RequestBondsH\x00\x12\x43\n\x04\x65tfs\x18\x02 \x01(\x0b\x32\x33.degiro_connector.trading.ProductSearch.RequestETFsH\x00\x12\x45\n\x05\x66unds\x18\x03 \x01(\x0b\x32\x34.degiro_connector.trading.ProductSearch.RequestFundsH\x00\x12I\n\x07\x66utures\x18\x04 \x01(\x0b\x32\x36.degiro_connector.trading.ProductSearch.RequestFuturesH\x00\x12O\n\nleverageds\x18\x05 \x01(\x0b\x32\x39.degiro_connector.trading.ProductSearch.RequestLeveragedsH\x00\x12G\n\x06lookup\x18\x06 \x01(\x0b\x32\x35.degiro_connector.trading.ProductSearch.RequestLookupH\x00\x12I\n\x07options\x18\x07 \x01(\x0b\x32\x36.degiro_connector.trading.ProductSearch.RequestOptionsH\x00\x12G\n\x06stocks\x18\x08 \x01(\x0b\x32\x35.degiro_connector.trading.ProductSearch.RequestStocksH\x00\x12K\n\x08warrants\x18\t \x01(\x0b\x32\x37.degiro_connector.trading.ProductSearch.RequestWarrantsH\x00\x42\t\n\x07request2\xcf\x13\n\x0cTradingRelay\x12u\n\rconfirm_order\x12,.degiro_connector.trading_relay.ConfirmOrder\x1a\x34.degiro_connector.trading.Order.ConfirmationResponse\"\x00\x12j\n\x0eproduct_search\x12-.degiro_connector.trading_relay.ProductSearch\x1a\'.degiro_connector.trading.ProductSearch\"\x00\x12U\n\nset_config\x12).degiro_connector.trading_relay.SetConfig\x1a\x1a.google.protobuf.BoolValue\"\x00\x12\x62\n\x0b\x63heck_order\x12\x1f.degiro_connector.trading.Order\x1a\x30.degiro_connector.trading.Order.CheckingResponse\"\x00\x12\x41\n\x07\x63onnect\x12\x16.google.protobuf.Empty\x1a\x1c.google.protobuf.StringValue\"\x00\x12J\n\x0c\x64\x65lete_order\x12\x1c.google.protobuf.StringValue\x1a\x1a.google.protobuf.BoolValue\"\x00\x12\x45\n\x10get_account_info\x12\x16.google.protobuf.Empty\x1a\x17.google.protobuf.Struct\"\x00\x12v\n\x14get_account_overview\x12\x31.degiro_connector.trading.AccountOverview.Request\x1a).degiro_connector.trading.AccountOverview\"\x00\x12Z\n\nget_agenda\x12(.degiro_connector.trading.Agenda.Request\x1a .degiro_connector.trading.Agenda\"\x00\x12}\n\x17get_cash_account_report\x12\x33.degiro_connector.trading.CashAccountReport.Request\x1a+.degiro_connector.trading.CashAccountReport\"\x00\x12G\n\x12get_client_details\x12\x16.google.protobuf.Empty\x1a\x17.google.protobuf.Struct\"\x00\x12_\n\x13get_company_profile\x12\x1c.google.protobuf.StringValue\x1a(.degiro_connector.trading.CompanyProfile\"\x00\x12]\n\x12get_company_ratios\x12\x1c.google.protobuf.StringValue\x1a\'.degiro_connector.trading.CompanyRatios\"\x00\x12?\n\nget_config\x12\x16.google.protobuf.Empty\x1a\x17.google.protobuf.Struct\"\x00\x12U\n\x13get_favourites_list\x12\x16.google.protobuf.Empty\x1a$.degiro_connector.trading.Favourites\"\x00\x12i\n\x18get_financial_statements\x12\x1c.google.protobuf.StringValue\x1a-.degiro_connector.trading.FinancialStatements\"\x00\x12g\n\x0fget_latest_news\x12,.degiro_connector.trading.LatestNews.Request\x1a$.degiro_connector.trading.LatestNews\"\x00\x12q\n\x13get_news_by_company\x12/.degiro_connector.trading.NewsByCompany.Request\x1a\'.degiro_connector.trading.NewsByCompany\"\x00\x12p\n\x12get_orders_history\x12/.degiro_connector.trading.OrdersHistory.Request\x1a\'.degiro_connector.trading.OrdersHistory\"\x00\x12_\n\x13get_products_config\x12\x16.google.protobuf.Empty\x1a..degiro_connector.trading.ProductSearch.Config\"\x00\x12m\n\x11get_products_info\x12..degiro_connector.trading.ProductsInfo.Request\x1a&.degiro_connector.trading.ProductsInfo\"\x00\x12Z\n\x14get_top_news_preview\x12\x16.google.protobuf.Empty\x1a(.degiro_connector.trading.TopNewsPreview\"\x00\x12\x82\x01\n\x18get_transactions_history\x12\x35.degiro_connector.trading.TransactionsHistory.Request\x1a-.degiro_connector.trading.TransactionsHistory\"\x00\x12^\n\nget_update\x12,.degiro_connector.trading.Update.RequestList\x1a .degiro_connector.trading.Update\"\x00\x12>\n\x06logout\x12\x16.google.protobuf.Empty\x1a\x1a.google.protobuf.BoolValue\"\x00\x12M\n\x0cupdate_order\x12\x1f.degiro_connector.trading.Order\x1a\x1a.google.protobuf.BoolValue\"\x00\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'degiro_connector.trading.models.trading_relay_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _SETCONFIG._serialized_start=225
  _SETCONFIG._serialized_end=318
  _CONFIRMORDER._serialized_start=320
  _CONFIRMORDER._serialized_end=437
  _PRODUCTSEARCH._serialized_start=440
  _PRODUCTSEARCH._serialized_end=1131
  _TRADINGRELAY._serialized_start=1134
  _TRADINGRELAY._serialized_end=3645
# @@protoc_insertion_point(module_scope)
