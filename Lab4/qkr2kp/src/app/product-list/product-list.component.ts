import { Component } from '@angular/core';

import { products } from '../products';

@Component({
  selector: 'app-product-list',
  templateUrl: './product-list.component.html',
  styleUrls: ['./product-list.component.css']
})
export class ProductListComponent {
  products = [...products];
  filteredProducts = [...products];
  pickedCategory = 'None';

  share(name:string, url:string) {
    window.open(`https://telegram.me/share/url?url=Welcome, купить ${name} &text= по ссылке ${url}`);
  }

  filterList(){
    if (this.pickedCategory == 'None') {
      this.filteredProducts = this.products;
    }
    else {
      this.filteredProducts = this.products.filter(p => p.category === this.pickedCategory);
    }
  }

  updateFilter(category: string) {
    this.pickedCategory = category;
    this.filterList();
  }

  deleteItem(id: number) {
    this.products = this.products.filter(p => p.id != id);
    this.filterList();
  }
}


/*
Copyright Google LLC. All Rights Reserved.
Use of this source code is governed by an MIT-style license that
can be found in the LICENSE file at https://angular.io/license
*/