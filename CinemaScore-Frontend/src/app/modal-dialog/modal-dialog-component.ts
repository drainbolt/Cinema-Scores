import { Component, Input } from "@angular/core";

@Component ({
    selector: 'modal-dialog',
    templateUrl: './modal-dialog.html',
    styleUrls: ['./modal-dialog.css']
})

export class ModalDialogComponent {
    @Input() movie;
}