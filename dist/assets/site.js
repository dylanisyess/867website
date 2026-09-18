const toggle=document.querySelector('.mobile-toggle');
const nav=document.querySelector('.main-nav');
toggle?.addEventListener('click',()=>{const open=toggle.getAttribute('aria-expanded')!=='true';toggle.setAttribute('aria-expanded',String(open));nav.classList.toggle('open',open);toggle.textContent=open?'Close':'Menu';});
const menus=[...document.querySelectorAll('.nav-group')];
menus.forEach(menu=>menu.addEventListener('toggle',()=>{if(menu.open)menus.filter(other=>other!==menu).forEach(other=>other.open=false);}));
document.addEventListener('click',event=>{if(!event.target.closest('.nav-group'))menus.forEach(menu=>menu.open=false);});
document.addEventListener('keydown',event=>{if(event.key==='Escape'){const active=menus.find(menu=>menu.open);if(active){active.open=false;active.querySelector('summary').focus();}else if(nav.classList.contains('open')){nav.classList.remove('open');toggle.setAttribute('aria-expanded','false');toggle.textContent='Menu';toggle.focus();}}});
document.querySelectorAll('[data-filter-group]').forEach(group=>{
 const filters=[...group.querySelectorAll('select[data-filter]')];
 const items=[...group.querySelectorAll('[data-filter-item]')];
 const run=()=>{let count=0;items.forEach(item=>{const match=filters.every(f=>!f.value||item.dataset[f.dataset.filter]===f.value);item.hidden=!match;if(match)count++;});group.querySelector('[data-count]').textContent=`${count} ${count===1?'item':'items'}`;const empty=group.querySelector('[data-filter-empty]');if(empty)empty.hidden=count>0;};
 filters.forEach(filter=>filter.addEventListener('change',run));run();
});
const dialog=document.querySelector('.lightbox');
if(dialog){document.querySelectorAll('.photo-open').forEach(button=>button.addEventListener('click',()=>{const img=button.querySelector('img');dialog.querySelector('img').src=button.dataset.full||img.src;dialog.querySelector('img').alt=img.alt;dialog.querySelector('[data-caption]').textContent=button.dataset.caption;dialog.showModal();}));dialog.querySelector('.dialog-close').addEventListener('click',()=>dialog.close());dialog.addEventListener('click',event=>{if(event.target===dialog){const r=dialog.getBoundingClientRect();if(event.clientX<r.left||event.clientX>r.right||event.clientY<r.top||event.clientY>r.bottom)dialog.close();}});}
dialog?.addEventListener('keydown',event=>{if(event.key==='Tab'){event.preventDefault();dialog.querySelector('.dialog-close').focus();}});
