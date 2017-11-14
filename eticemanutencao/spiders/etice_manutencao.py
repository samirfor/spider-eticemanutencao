# -*- coding: utf-8 -*-
import scrapy


class EticeManutencaoSpider(scrapy.Spider):
    name = "etice-manutencao"
    allowed_domains = ["avisosdemanutencao.etice.ce.gov.br"]
    start_urls = ['http://avisosdemanutencao.etice.ce.gov.br/']

    def parse(self, response):
        for row in response.xpath('/html/body/div[2]/div/table/tbody/tr'):
            yield {
                'data_publicacao_atualizacao': row.xpath('./td[1]//text()').extract_first(default='').strip(),
                'problema': row.xpath('./td[2]//text()').extract_first(default='').strip(),
                'unidade': row.xpath('./td[3]//text()').extract_first(default='').strip(),
                'data_ocorrencia': row.xpath('./td[4]//text()').extract_first(default='').strip(),
                'acompanhamento': row.xpath('./td[5]//text()').extract_first(default='').strip(),
                'afetados': row.xpath('./td[6]//text()').extract_first(default='').strip(),
                'previsao': row.xpath('./td[7]//text()').extract_first(default='').strip(),
                'status': row.xpath('./td[8]//text()').extract_first(default='').strip(),
            }
